from PIL import Image as PILImage
import numpy as np


def convert_to_grayscale(image):
    return image.convert("L")  # Convert to grayscale

# Function to flatten the pixel array
def flatten_pixel_array(image):
    pixel_array = np.array(image)  # Convert to 2D NumPy array
    return pixel_array.flatten()     # Flatten to 1D NumPy array

# Function to load an image from the given path
def load_image(image_path):
    try:
        # Load the image
        image = PILImage.open(image_path)
         # Convert to grayscale
        gray_image = convert_to_grayscale(image)
        return gray_image
    except Exception as e:
        print(f"Error loading image: {e}")
        return None

def xor_binary_strings(str1, str2):
    """Performs XOR operation between two binary strings."""
    result = ""
    for i in range(len(str1)):
        if str1[i] == str2[i]:
            result += "0"
        else:
            result += "1"
    return result

def numpy_to_binary(arr):
    """Converts a NumPy array of integers to a string of binary."""
    binary_string = ""
    for value in arr:
        binary_val = format(value, '08b')  # Convert to binary with leading zeros
        binary_string += binary_val
    return binary_string

def binary_to_numpy_array(binary_string):
    """Converts a binary string to a NumPy array of integers."""
    int_list = []
    for i in range(0, len(binary_string), 8):
        byte_string = binary_string[i:i + 8]
        int_list.append(int(byte_string, 2))
    return np.array(int_list)

# Specify the paths to your images here
plain_image_path = "D:\\Documents\\img1.jpg"  # Change to your plain image path

# Load the plain image
plain_image = load_image(plain_image_path)

if plain_image is not None:
    # Convert the plain image to NumPy array
    plain_pixel_array = np.array(plain_image)

    # Flatten the pixel array
    plain_flattened_array = flatten_pixel_array(plain_image)

    # Convert flattened array to binary
    binary_image = numpy_to_binary(plain_flattened_array)

    # Select the key image path from user input for encryption
    key_image_path = input("Enter the path for the key image: ")  # Prompt user for key image path
    key_image = load_image(key_image_path)

    if key_image is not None:
        key_pixel_array = np.array(key_image)
        key_flattened_array = flatten_pixel_array(key_image)

        # Convert flattened key array to binary
        binary_key = numpy_to_binary(key_flattened_array)

        # Perform XOR operation for encryption
        xor_result = xor_binary_strings(binary_image, binary_key)
        
        # Convert the encrypted binary result back to a NumPy array
        encrypted_numpy_array = binary_to_numpy_array(xor_result)

        # Reshape the encrypted NumPy array to the original image dimensions
        encrypted_image_array = encrypted_numpy_array.reshape(plain_pixel_array.shape)

        # Create a PIL image from the encrypted NumPy array
        encrypted_image = PILImage.fromarray(encrypted_image_array.astype(np.uint8))
        encrypted_image.show()  # Show the encrypted image

        # Prompt user for key image path for decryption
        decrypt_key_image_path = input("Enter the path for the key image to decrypt: ")  # Prompt for decryption key
        decrypt_key_image = load_image(decrypt_key_image_path)

        if decrypt_key_image is not None:
            # Flatten and convert the decryption key image to binary
            decrypt_key_flattened_array = flatten_pixel_array(decrypt_key_image)
            decrypt_binary_key = numpy_to_binary(decrypt_key_flattened_array)

            # Decrypt the image
            decrypted_xor_result = xor_binary_strings(xor_result, decrypt_binary_key)

            # Convert the decrypted XOR result back to a NumPy array
            decrypted_numpy_array = binary_to_numpy_array(decrypted_xor_result)

            # Reshape the decrypted NumPy array to the original image dimensions
            decrypted_image_array = decrypted_numpy_array.reshape(plain_pixel_array.shape)

            # Create a PIL image from the decrypted NumPy array
            decrypted_image = PILImage.fromarray(decrypted_image_array.astype(np.uint8))
            decrypted_image.show()  # Show the decrypted image
        else:
            print("Failed to load the decryption key image.")
    else:
        print("Failed to load the key image for encryption.")
else:
    print("Failed to load the plain image.")











