import socket
from datetime import datetime


class PortScanner:
    def __init__(self, target):
        self.target = target
        self.open_ports = {}

    def scan_port(self, port, scan_versions=False):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((self.target, port))
        sock.close()

        if scan_versions and result == 0:
            service = socket.getservbyport(port)
            self.open_ports[port] = service

        return result

    def scan_all_ports(self, ports, scan_versions=False):
        open_ports = []

        for port in ports:
            scan_result = self.scan_port(port, scan_versions)
            if scan_result == 0 and not scan_versions:
                open_ports.append(port)

        return open_ports

    def scan_single_port(self, port, scan_versions=False):
        scan_result = self.scan_port(port, scan_versions)
        return scan_result

def main():
    print("Burhan Yaşbay")
    print("Port Tarayıcıya Hoş Geldiniz!")
    target_ip = input("Hedef IP adresini girin: ")
    
    print("-" * 45)
    print("Port tarama seçenekleri:")
    print("1. Tüm portları tarat")
    print("2. Tek bir port tara")
    print("3. Çıkış")
    print("-" * 45)
    
    option = input("Seçeneğinizi girin (1/2/3): ")
    
    if option == "3":
        return
    
    scanner = PortScanner(target_ip)
    
    if option == "1":
        scan_versions = input("Versiyon taraması yapmak istiyor musunuz? (E/H): ").lower()
        if scan_versions == "e":
            scan_versions = True
        else:
            scan_versions = False

        print("-" * 45)
        print("Hedef IP adresi taraması başlıyor...")
        print("Tarama başlangıç tarihi:", datetime.now())
        
        ports_to_scan = range(1, 65536)
        open_ports = scanner.scan_all_ports(ports_to_scan, scan_versions)

        if open_ports:
            print("-" * 45)
            print("Açık portlar:")
            for port in open_ports:
                if scan_versions:
                    service = scanner.open_ports.get(port, "Bilinmeyen Servis")
                    print(f"Port {port} açık. Servis: {service}")
                else:
                    print(f"Port {port} açık")
            print("-" * 45)
        else:
            print("Açık port bulunamadı.")
    
    elif option == "2":
        port_to_scan = int(input("Taramak istediğiniz port numarasını girin: "))
        scan_versions = input("Versiyon taraması yapmak istiyor musunuz? (E/H): ").lower()
        if scan_versions == "e":
            scan_versions = True
        else:
            scan_versions = False

        print("-" * 45)
        print("Hedef IP adresi taraması başlıyor...")
        print("Tarama başlangıç tarihi:", datetime.now())
        
        scan_result = scanner.scan_single_port(port_to_scan, scan_versions)
        if scan_result == 0:
            if scan_versions:
                service = scanner.open_ports.get(port_to_scan, "Bilinmeyen Servis")
                print("-" * 45)
                print(f"Port {port_to_scan} açık. Servis: {service}")
                print("-" * 45)
            else:
                print("-" * 45)
                print(f"Port {port_to_scan} açık.")
                print("-" * 45)
        else:
            print("-" * 45)
            print(f"Port {port_to_scan} kapalı.")
            print("-" * 45)
    
    else:
        print("Geçersiz seçenek. Lütfen 1, 2 veya 3 seçeneğini girin.")

if __name__ == "__main__":
    main()