import matplotlib.pyplot as plt

# Data for fixed key size and varying message sizes
message_sizes = ["1st message", "29", "1,2,3,4 & 5 and 999999999",
                 "Longer text message to test the RSA algorithm",
                 "1,2,3 hello! Hello! Anyone there?"]
key_256 = [0.0034, 0.00, 0.0037, 0.0112, 0.0048]
key_384 = [0.006, 0.001, 0.0087, 0.022, 0.0099]
key_512 = [0.0179, 0.002, 0.0135, 0.0508, 0.025]
key_1024 = [0.1022, 0.0072, 0.089, 0.3454, 0.1447]
key_2048 = [0.616, 0.0443, 0.7237, 2.0397, 0.956]

# Plotting fixed key size and varying message sizes
plt.figure(figsize=(12, 6))
plt.plot(message_sizes, key_256, label='256-bit Key')
plt.plot(message_sizes, key_384, label='384-bit Key')
plt.plot(message_sizes, key_512, label='512-bit Key')
plt.plot(message_sizes, key_1024, label='1024-bit Key')
plt.plot(message_sizes, key_2048, label='2048-bit Key')
plt.xlabel('Message Size')
plt.ylabel('Time (seconds)')
plt.title('Encryption/Decryption Time vs. Message Size (Fixed Key Size)')
plt.legend()
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# Data for fixed message size and varying key sizes
key_sizes = [256, 384, 512, 1024, 2048]
gen_times = [0.0022, 0.003, 0.0034, 0.1433, 0.6362]
enc_times = [0.0034, 0.006, 0.0179, 0.1022, 0.616]
dec_times = [0.0032, 0.0069, 0.0159, 0.1039, 0.5881]

# Plotting fixed message size and varying key sizes
plt.figure(figsize=(12, 6))
plt.plot(key_sizes, gen_times, label='Key Generation Time')
plt.plot(key_sizes, enc_times, label='Encryption Time')
plt.plot(key_sizes, dec_times, label='Decryption Time')
plt.xlabel('Key Size (bits)')
plt.ylabel('Time (seconds)')
plt.title('Key Generation, Encryption, and Decryption Time vs. Key Size (Fixed Message Size)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
