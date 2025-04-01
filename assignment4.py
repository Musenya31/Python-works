def modify_file(input_filename, output_filename):
    try:
        # Open the input file for reading
        with open(input_filename, "r") as input_file:
            content = input_file.read()

        # Modify the content (e.g., convert to uppercase)
        modified_content = content.upper()  # Example: make text uppercase

        # Write the modified content to the output file
        with open(output_filename, "w") as output_file:
            output_file.write(modified_content)

        print(f"Modified content has been written to '{output_filename}' successfully.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except PermissionError:
        print(f"Error: You do not have permission to access '{input_filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Main program
try:
    input_filename = input("Enter the name of the file to read: ")
    output_filename = input("Enter the name of the file to write to: ")

    modify_file(input_filename, output_filename)

except KeyboardInterrupt:
    print("\nOperation interrupted by the user.")
