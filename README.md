# Undazomen

An advanced high-compression Zip-Bomb generator for penetration testing and security analysis.

## Description

Undazomen is a specialized tool designed for professionals who need to generate test ZIPBOMB files with specific multi-level compression characteristics. The tool creates files with deep recursive structure and multiple compression layers.

## How It Works (The Magic Behind the Madness)

Imagine you have a massive warehouse full of identical boxes. Now, what if you could compress each box into a grain of rice, then compress 15 grains of rice into another grain of rice, and repeat this process 9 times? That's essentially what Undazomen does with data.

### The Compression Cascade

Here's the process:

1. **Start Big**: Generate 512MB of highly compressible data patterns
2. **Squeeze Hard**: Use Zstandard compression to crush it down ~32,000x smaller
3. **Nest the Nightmare**: Take that compressed data and compress it again... and again... and again
4. **Multiply the Mayhem**: Create multiple copies at each layer to amplify the effect

### Why It's Ridiculously Efficient

| Step | What Happens | Size Transform |
|------|--------------|----------------|
| **Initial** | Generate 512MB of repetitive patterns | 512MB → 512MB |
| **Layer 1** | Zstandard compression crushes the patterns | 512MB → 16KB |
| **Layer 2-9** | Each layer compresses the previous result | 16KB → 8KB → 4KB... |
| **Final Zip** | Package everything with decoy files | Result: ~78KB |
| **Extraction** | Recursive decompression explodes exponentially | **78KB → 5.8TB** |

**Repetitive data compresses insanely well**, and when you stack compressions on top of each other, the math gets absolutely wild. It's like compound interest, but for file size explosions.

### Real-World Impact

When someone tries to extract your innocent-looking 78KB file:
- Their system allocates memory for 5.8TB of data
- Hard drives start crying
- RAM gets obliterated
- System processes grind to a halt

The computer dutifully follows the compression instructions, unaware it's being asked to materialize terabytes from kilobytes.

### Why This Beats Old-School Zipbombs

Traditional zipbombs were basically one-trick ponies. They'd stuff a massive file into a ZIP and call it a day. Here's why Undazomen laughs at those amateur attempts:

| Old Zipbombs | Undazomen | Why It Matters |
|--------------|-----------|----------------|
| Single compression layer | Up to 9 nested layers | Exponential vs linear growth |
| Basic file duplication | Smart pattern generation | Better compression ratios |
| Fixed structure | Dynamic multi-algorithm approach | Harder to detect/filter |
| ~1000x compression | **30,000x+ compression** | Insane efficiency boost |
| Predictable behavior | Randomized output names | Evades simple signatures |

**The Real Difference**: Old zipbombs were like throwing a big rock. Undazomen is like nuclear fission - each compression layer multiplies the effect. While classic zipbombs might get you 1GB from 1MB, Undazomen casually delivers 5.8TB from 78KB.

**Detection Evasion**: Traditional zipbombs had obvious signatures. Undazomen includes decoy files, realistic filenames, and variable structures that make it look like legitimate software updates or document archives.

## Features

- **Multi-Level Compression**: Implements up to 9 recursive compression layers
- **Multiple Algorithms**: Uses Zstandard and DEFLATE for maximum optimization
- **Parallel Generation**: Multi-threaded processing for enhanced efficiency
- **Decoy Files**: Includes fake documents to simulate legitimate content
- **System Monitoring**: Real-time visualization of resource usage
- **Professional Interface**: Terminal with colors and advanced progress bars

## System Requirements

- **Python**: 3.8 or higher
- **Operating System**: Windows 10/11, Linux, macOS
- **RAM**: Minimum 4GB (8GB recommended)
- **Disk Space**: 2GB free for temporary files

### Resource Estimation Table

| Depth | Copies | Compressed Size | Decompressed Size | RAM Required | Generation Time |
|-------|--------|-----------------|-------------------|--------------|-----------------|
| 3     | 5      | ~10 MB         | ~2.5 GB          | 1-2 GB       | 30-60 seconds   |
| 5     | 8      | ~500 KB        | ~40 GB           | 2-4 GB       | 1-2 minutes     |
| 7     | 12     | ~150 KB        | ~1.2 TB          | 4-6 GB       | 2-3 minutes     |
| 9     | 15     | ~78 KB         | ~5.8 TB          | 6-8 GB       | 3-5 minutes     |
| 12    | 20     | ~45 KB         | ~47 TB           | 8-12 GB      | 5-8 minutes     |

**Note**: Higher depth/copies values create smaller compressed files but exponentially larger decompressed sizes. The compression ratios can reach 30,000x or higher, making tiny files that expand to terabytes when extracted.

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Jefriline/Undazomen.git
cd Undazomen
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

## Usage

### Basic Execution

```bash
python main.py
```

### Parameter Customization

```python
# Modify in main.py line 280
generator = UndazomenGenerator(depth=10, copies=20)
```

**Available parameters:**
- `depth`: Number of compression layers (1-15)
- `copies`: Copies per layer (1-50)

### Example Output

```
  _   _           _                                      
 | | | |_ __   __| | __ _ _______  _ __ ___   ___ _ __  
 | | | | '_ \ / _` |/ _` |_  / _ \| '_ ` _ \ / _ \ '_ \ 
 | |_| | | | | (_| | (_| |/ / (_) | | | | | |  __/ | | |
  \___/|_| |_|\__,_|\__,_/___\___/|_| |_| |_|\___|_| |_|
        Advanced ZIPBOMB Generation System
                 Edition | v1.0 | 2025

System Resources:
  CPU: 15.2% | Memory: 45.8% | Disk: 48.8%
────────────────────────────────────────────────────────────
* Initializing weaponization engine
> Generating decoy files
[+] Created decoy: Financial_Report_Q3.docx
[+] Created decoy: Project_Timeline.pdf
[+] Created decoy: Technical_Specifications.xlsx
[+] Created decoy: User_Manual.txt
[+] Created decoy: Backup_Config.zip
> Crafting compression bomb core (Turbo Mode)
  Generating data:        [████████████████████████████████████████████████] 100.0% 512MB/512MB
  [+] Base payload: 512MB (Generated in turbo mode)
#1 Building archive layer 1/9
> Compressing layer 1/9
  Zstandard:              [████████████████████████████████████████████████] 100.0% 512MB → 16KB
  [+] Compression ratio: 32498.2x
  [+] Layer complete: 243KB
...
[+] Weaponized archive created: compressed_data_6840.zip
[+] Final size: 78KB | Estimated decompressed: >5TB

Compression Statistics:
  Layer 1: Zstandard - 512MB -> 16KB (Ratio: 32498.2x)
  Layer 2: Zstandard - 0MB -> 0KB (Ratio: 335.3x)
  Layer 3: Zstandard - 0MB -> 0KB (Ratio: 13.3x)
  Layer 4: DEFLATE - 0MB -> 1KB (Ratio: 12.1x)
  ...

Archive Structure:
compressed_data_XXXX.zip/
  ├─ docs/Financial_Report_Q3.docx
  ├─ docs/Project_Timeline.pdf
  ├─ CORE_DATA.dat
  └─ README.txt

[!] WARNING: This archive contains compressed payloads
    Handle with extreme caution. For authorized testing only.
```

## Project Structure

```
Undazomen/
├── main.py              # Main file
├── requirements.txt     # Python dependencies
├── README.md           # Documentation
└── releases/           # Release files
```

## Testing Capabilities

Undazomen generates compression bomb archives that can be used to test:

### **Decompression Tool Stress Testing**
- **Memory exhaustion**: Tests how decompression tools handle extremely large expanded data
- **Resource consumption**: Monitors CPU and memory usage during decompression
- **Archive parsing**: Tests behavior with deeply nested ZIP structures
- **Compression ratio handling**: Extreme compression ratios (30,000x+)

### **Security Assessment Uses**
- **Antivirus detection**: Test if security software detects compression bombs
- **System resource limits**: Verify system protection against resource exhaustion
- **Application resilience**: Test how applications handle malformed/extreme archives
- **Incident response**: Training scenarios for security teams

### **Generated Archive Features**
- **Multi-layer compression**: Up to 9 nested compression layers
- **Decoy files**: Legitimate-looking documents to test filtering
- **Cross-platform compatibility**: Works on Windows, Linux, and macOS
- **Configurable parameters**: Adjustable depth and file copies

**Note**: This tool creates compression bombs for testing purposes. It does not exploit specific CVEs but can help identify systems vulnerable to resource exhaustion attacks.

## Security Considerations

⚠️ **IMPORTANT WARNING**

This tool is designed exclusively for:
- Authorized penetration testing
- Security analysis in controlled environments
- Academic cybersecurity research
- Antivirus system evaluation
- Compression bomb testing and research

**DO NOT use for:**
- Production systems without authorization
- Corporate networks without explicit permissions
- Any malicious or illegal activity

## Troubleshooting

### Insufficient Memory Error

```bash
# Reduce generation parameters
generator = UndazomenGenerator(depth=5, copies=8)
```

### Permission Issues

```bash
# Windows: Run as administrator
# Linux: Check write permissions
chmod +x main.py
```

### Missing Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt --force-reinstall
```

## Known Limitations

⚠️ **Important Limitations to Consider:**

### **System Compatibility**
- **Mobile devices**: Not supported on Android/iOS (requires desktop Python environment)
- **Low-end systems**: Devices with <4GB RAM may crash or freeze
- **Virtual machines**: May require additional RAM allocation
- **Docker containers**: Ensure sufficient memory limits are set

### **Performance Constraints**
- **Generation time**: Can take 5-15 minutes for maximum settings
- **CPU intensive**: Will use 100% CPU during generation
- **Memory usage**: Can consume up to 12GB RAM for large configurations
- **Disk I/O**: Temporary files may reach several GB during processing

### **Usage Restrictions**
- **Production environments**: Never run on production systems
- **Network shares**: Avoid generating files on network drives (slow I/O)
- **Antivirus software**: May trigger false positives and slow generation
- **Concurrent execution**: Don't run multiple instances simultaneously

### **Technical Limitations**
- **File size limits**: Some systems have 4GB file size restrictions
- **Archive tools**: Not all decompression tools can handle extreme compression ratios
- **Platform differences**: Windows/Linux may show different performance characteristics

## Contributing

We welcome contributions to improve Undazomen! Here's how you can help:

### **How to Contribute**
1. **Fork the repository** on GitHub
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Make your changes** and test thoroughly
4. **Commit your changes**: `git commit -m 'Add amazing feature'`
5. **Push to your branch**: `git push origin feature/amazing-feature`
6. **Submit a Pull Request** with a detailed description

### **Contribution Guidelines**
- **Code quality**: Follow Python PEP 8 standards
- **Documentation**: Update README if adding new features
- **Testing**: Ensure your changes don't break existing functionality
- **Security**: Consider security implications of new features

### **Areas for Improvement**
- Performance optimizations for large files
- Additional compression algorithms
- Better error handling and recovery
- Cross-platform compatibility enhancements
- User interface improvements

### **Reporting Issues**
Found a bug or have a suggestion? Please:
1. Check existing issues first
2. Provide detailed reproduction steps
3. Include system information (OS, Python version, RAM)
4. Attach relevant log files if applicable

## License

This project is under the MIT License. See `LICENSE` file for more details.




**Legal Notice**: This tool is provided for educational and research purposes only. I am not responsible for misuse of this tool.
