def process_text_file(input_file, output_file):
    try:
        # Read the contents of input.txt
        with open(input_file, 'r') as file:
            content = file.read()

        # Count the number of words
        word_count = len(content.split())

        # Convert all text to uppercase
        upper_content = content.upper()

        # Prepare the output content
        output_content = f"{upper_content}\n\nWord Count: {word_count}"

        # Write the processed text and word count to output.txt
        with open(output_file, 'w') as file:
            file.write(output_content)

        # Print success message
        print(f"Success! '{output_file}' has been created with the processed content.")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function
process_text_file('input.txt', 'output.txt')
def modify_content(content):
    # Example modification: convert text to uppercase
    return content.upper()

def main():
    try:
        # 🧪 Ask for filename
        input_filename = input("Enter the name of the file to read: ")

        # 🖋️ Read the file
        with open(input_filename, 'r') as infile:
            original_content = infile.read()

        # Modify the content
        modified_content = modify_content(original_content)

        # Write to a new file
        output_filename = "modified_" + input_filename
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)

        print(f"Modified content written to '{output_filename}' successfully.")

    except FileNotFoundError:
        print("Error: The file does not exist. Please check the filename and try again.")
    except IOError:
        print("Error: Could not read the file. Please check permissions or file integrity.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
