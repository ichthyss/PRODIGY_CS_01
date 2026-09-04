# Caesar Cipher CLI

A small command-line tool for encoding and decoding messages with the Caesar cipher.

## Features

- Encrypt a message from the command line
- Decrypt a message from the command line
- Read input from a file
- Write output to a file
- Supports uppercase and lowercase letters while leaving non-letter characters unchanged

## Installation

```bash
pip install .
```

## Usage

### Encode a message

```bash
caesar -m "hello world" -s 3 -e
```

Example output:

```bash
khoor zruog
```

### Decode a message

```bash
caesar -m "khoor zruog" -s 3 -d
```

Example output:

```bash
hello world
```

### Encode from a file

```bash
caesar -f input.txt -s 3 -e -out output.txt
```

### Decode from a file

```bash
caesar -f input.txt -s 3 -d -out output.txt
```

