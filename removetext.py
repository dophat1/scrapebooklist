def remove_unwanted_text(input_file, output_file, unwanted_phrases):
    """
    Removes unwanted text from a file.

    :param input_file: Path to the input text file.
    :param output_file: Path to save the cleaned text.
    :param unwanted_phrases: A list of phrases to remove.
    """
    try:
        # Read the input file
        with open(input_file, "r", encoding="utf-8") as file:
            text = file.read()

        # Remove unwanted phrases
        for phrase in unwanted_phrases:
            text = text.replace(phrase, "")

        # Write the cleaned text to the output file
        with open(output_file, "w", encoding="utf-8") as file:
            file.write(text)

        print(f"Text cleaned and saved to {output_file}.")
    except FileNotFoundError:
        print(f"Error: {input_file} not found.")
    except IOError as e:
        print(f"Error processing file: {e}")

# Example usage
if __name__ == "__main__":
    # Specify the input and output file paths
    input_path = "books_data.txt"
    output_path = "output.txt"

    # Define phrases to remove
    phrases_to_remove = [
        "[FREE DOWNLOAD]Xem nhiều hơn",
        "EBOOK",
        "TẢI MIỄN PHÍ EBOOK: ",
        "DOWNLOAD MIỄN PHÍ EBOOK HAY: ",
        "DOWNLOAD SÁCH: ",
        "TẢI MIỄN PHÍ : ",
        "DOWNLOAD MIỄN PHÍ : ",
        "Xem nhiều hơn",
        "DOWNLOAD MIỄN PHÍ  HAY: ",
        "DOWNLOAD : ",
        "TẢI MIỄN PHÍ: ",
        "[FREE DOWNLOAD]  ",
        "KINDLE HAY: "
    ]

    # Call the function
    remove_unwanted_text(input_path, output_path, phrases_to_remove)
