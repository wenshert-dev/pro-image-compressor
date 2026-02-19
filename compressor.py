import os
import time
import argparse
from PIL import Image
from tqdm import tqdm
from colorama import Fore, Style, init

# Renkli terminal çıktıları için başlatma
init(autoreset=True)

class ImageOptimizer:
    def __init__(self, quality=85):
        self.quality = quality
        self.stats = []

    def get_size_format(self, b, factor=1024, suffix="B"):
        """Boyutları okunabilir formata çevirir (KB, MB vb.)"""
        for unit in ["", "K", "M", "G", "T", "P"]:
            if b < factor:
                return f"{b:.2f}{unit}{suffix}"
            b /= factor

    def optimize(self, input_path, output_folder):
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # Desteklenen formatlar
        valid_extensions = ('.jpg', '.jpeg', '.png', '.webp')
        files = [f for f in os.listdir(input_path) if f.lower().endswith(valid_extensions)]
        
        print(f"{Fore.CYAN}🚀 İşlem başlatılıyor: {len(files)} dosya bulundu.\n")

        for filename in tqdm(files, desc="Sıkıştırılıyor", unit="resim"):
            in_file = os.path.join(input_path, filename)
            out_file = os.path.join(output_folder, filename)
            
            # Orijinal boyut
            initial_size = os.path.getsize(in_file)
            
            try:
                with Image.open(in_file) as img:
                    # RGB'ye çevir (PNG'den JPEG'e geçerken hata almamak için)
                    if img.mode in ("RGBA", "P"):
                        img = img.convert("RGB")
                    
                    img.save(out_file, optimize=True, quality=self.quality)
                
                # Yeni boyut ve kazanç hesaplama
                final_size = os.path.getsize(out_file)
                ratio = (1 - (final_size / initial_size)) * 100
                self.stats.append((filename, initial_size, final_size, ratio))
                
            except Exception as e:
                print(f"{Fore.RED}\n[!] Hata: {filename} işlenemedi. -> {e}")

    def show_summary(self):
        """İşlem bitince havalı bir özet tablosu basar"""
        print(f"\n{Fore.GREEN}{'='*60}")
        print(f"{'DOSYA ADI':<25} | {'ESKİ':<10} | {'YENİ':<10} | {'KUCULTME'}")
        print(f"{'='*60}")
        
        total_saved = 0
        for name, old, new, ratio in self.stats:
            total_saved += (old - new)
            short_name = (name[:22] + '..') if len(name) > 22 else name
            print(f"{short_name:<25} | {self.get_size_format(old):<10} | {self.get_size_format(new):<10} | %{ratio:.1f}")
        
        print(f"{'='*60}")
        print(f"{Fore.YELLOW}Toplam Tasarruf: {self.get_size_format(total_saved)}")
        print(f"{Fore.GREEN}{'='*60}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Pro Image Compressor CLI")
    parser.add_argument("-i", "--input", default=".", help="Giriş klasörü (Varsayılan: bulunduğun dizin)")
    parser.add_argument("-o", "--output", default="compressed", help="Çıkış klasörü")
    parser.add_argument("-q", "--quality", type=int, default=70, help="Kalite (1-95 arası)")

    args = parser.parse_args()

    compressor = ImageOptimizer(quality=args.quality)
    compressor.optimize(args.input, args.output)
    compressor.show_summary()