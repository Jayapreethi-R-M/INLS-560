__author__ = 'Jayapreethi Radhakrishnan Madanraj, jayam@ad.unc.edu, Onyen = jayam'

# Loads data for both books and movies, returning a dictionary with two keys, 'books' and 'movies', one for
# each subset of the collection.
def load_collections():
    # Load the two collections.
    book_collection, max_book_id = load_collection("books.csv")
    movie_collection, max_movie_id = load_collection("movies.csv")

    # Check for error.
    if book_collection is None or movie_collection is None:
        return None, None

    # Return the composite dictionary.
    return {"books": book_collection, "movies": movie_collection}, max(max_book_id, max_movie_id)


# Loads a single collection and returns the data as a dictionary.  Upon error, None is returned.
def load_collection(file_name):
    max_id = -1
    try:
        # Create an empty collection.
        collection = {}

        # Open the file and read the field names
        collection_file = open(file_name, "r")
        field_names = collection_file.readline().rstrip().split(",")

        # Read the remaining lines, splitting on commas, and creating dictionaries (one for each item)
        for item in collection_file:
            field_values = item.rstrip().split(",")
            collection_item = {}
            for index in range(len(field_values)):
                if (field_names[index] == "Available") or (field_names[index] == "Copies") or (field_names[index] == "ID"):
                    collection_item[field_names[index]] = int(field_values[index])
                else:
                    collection_item[field_names[index]] = field_values[index]
            # Add the full item to the collection.
            collection[collection_item["ID"]] = collection_item
            # Update the max ID value
            max_id = max(max_id, collection_item["ID"])

        # Close the file now that we are done reading all of the lines.
        collection_file.close()

    # Catch IO Errors, with the File Not Found error the primary possible problem to detect.
    except FileNotFoundError:
        print("File not found when attempting to read", file_name)
        return None
    except IOError:
        print("Error in data file when reading", file_name)
        return None

    # Return the collection.
    return collection, max_id


# Display the menu of commands and get user's selection.  Returns a string with  the user's reauexted command.
# No validation is performed.
def prompt_user_with_menu():
    print("\n\n********** Welcome to the Collection Manager. **********")
    print("COMMAND    FUNCTION")
    print("  ci         Check in an item")
    print("  co         Check out an item")
    print("  ab         Add a new book")
    print("  am         Add a new movie")
    print("  db         Display books")
    print("  dm         Display movies")
    print("  qb         Query for books")
    print("  qm         Query for movies")
    print("  x          Exit")
    return input("Please enter a command to proceed: ")

def check_in(collections):
    try:
        # Asking user for id of the item to be checked in.
        id = int(input("Enter the ID for the item you wish to check in: "))
        # Checking if the id is in books.
        if id in collections['books'].keys():
            # Checking if the book is actually missing, if missing, its checked in.
            if collections['books'][id]['Copies'] > collections['books'][id]['Available'] and collections['books'][id]['Available'] >= 0:
                # Availability is updated and notified.
                collections['books'][id]['Available'] += 1
                print("Your check in has succeeded.")
                result = '\n'.join(f'{key}: {value}' for key, value in collections['books'][id].items())
                print('\n', result, sep='')
            else:
                # Letting user know that the book was not checked out in first place.
                print("All copies are already available, so this item can not be checked in.")
        # Checking if the id is in movies.
        if id in collections['movies'].keys():
            # Checking if the movie is actually missing, if missing, its checked in.
            if ((int(collections['movies'][id]['Copies'])) > (int(collections['movies'][id]['Available']))) and ((int(collections['movies'][id]['Available'])) >= 0):
                # Availability is updated and notified.
                collections['movies'][id]['Available'] += 1
                print("Your check in has succeeded.")
                print(collections['movies'][id])
                result = '\n'.join(f'{key}: {value}' for key, value in collections['movies'][id].items())
                print('\n', result, sep='')
            else:
                # Letting user know that the movie was not checked out in fist place.
                print("All copies are already available, so this item can not be checked in.")
        # Letting user know that the ID is invalid.
        if id not in collections['books'].keys() and id not in collections['movies'].keys():
            print("ID not found.")
    except Exception as error:
        print("Error: ", error)

def check_out(collections):
    try:
        # Asking user for id of the item to be checked in.
        id = int(input("Enter the ID for the item you wish to check out: "))
        # Checking if the id is in books.
        if id in collections['books'].keys():
            # Checking if the book is available, if yes, its checked out.
            if collections['books'][id]['Copies'] >= collections['books'][id]['Available'] and collections['books'][id]['Available'] > 0:
                # Availability is updated and notified.
                collections['books'][id]['Available'] -= 1
                print("Your check out has succeeded.")
                result = '\n'.join(f'{key}: {value}' for key, value in collections['books'][id].items())
                print('\n', result, sep='')
            else:
                # Letting user know that the book is not avaiable to be checked out.
                print("No copies of the item are available for check out.")
        # Checking if the id is in movies.
        if id in collections['movies'].keys():
        # Checking if the movie is available, if yes, its checked out.
            if ((int(collections['movies'][id]['Copies'])) >= (int(collections['movies'][id]['Available']))) and ((int(collections['movies'][id]['Available'])) > 0):
                # Availability is updated and notified.
                collections['movies'][id]['Available'] -= 1
                result = '\n'.join(f'{key}: {value}' for key, value in collections['movies'][id].items())
                print('\n', result, sep='')
            else:
                # Letting user know that the movie is not avaiable to be checked out.
                print("No copies of the item are available for check out.")
        # Letting user know that the ID is invalid.
        if id not in collections['books'].keys() and id not in collections['movies'].keys():
            print("ID not found.")
    except Exception as error:
        print("Error: ", error)

def add_book(collection, max_id):
    try:
        # Setting the id for the new book to be added by taking the max of the book ids and adding one.
        id = max_id + 1
        # Creating a new dict to collect the user inputs and taking user input.
        collection[id] = {}
        collection[id]['Title'] = input("Title: ")
        collection[id]['Author'] = input("Author: ")
        collection[id]['Publisher'] = input("Publisher: ")
        collection[id]['Pages'] = input("Pages: ")
        collection[id]['Year'] = input("Year: ")
        collection[id]['Copies'] = input("Copies: ")
        collection[id]['Available'] = collection[id]['Copies']
        # Printing the user inputs.
        print("You have entered the following data:")
        print("ID:", id)
        [print(key, ':', value) for key, value in collection[id].items()]
        # Taking user inputs to add the book or not.
        add_or_not = input("Press enter to add this item to the collection.  Enter 'x' to cancel.")
        # Book added, moving on to menu.
        if add_or_not == '':
            # Updating the max id to enable adding another book with unique id if needed and returning it.
            max_id = max_id + 1
            return max_id
            prompt_user_with_menu()
        # Deleting the book as per user wish.
        elif add_or_not == 'x' or add_or_not == 'X':
            del collection[id]
    except Exception as error:
        print("Error: ", error)

def add_movie(collection, max_id):
    try:
        # Setting the id for the new movie to be added by taking the max of the movie ids and adding one.
        id = max_id + 1
        # creating a new dict to collect the user inputs and taking user input.
        collection[id] = {}
        collection[id]['Title'] = input("Title: ")
        collection[id]['Director'] = input("Director: ")
        collection[id]['Length'] = input("Length: ")
        collection[id]['Genre'] = input("Genre: ")
        collection[id]['Year'] = input("Year: ")
        collection[id]['Copies'] = input("Copies: ")
        collection[id]['Available'] = collection[id]['Copies']
        print("You have entered the following data:")
        print("ID:", id)
        [print(key, ':', value) for key, value in collection[id].items()]
        # Taking user inputs to add the movie or not.
        add_or_not = input("Press enter to add this item to the collection.  Enter 'x' to cancel.")
        # Book added, moving on to menu.
        if add_or_not == '':
            # Updating the max id to enable adding another movie with unique id if needed and returning it.
            max_id = max_id + 1
            return max_id
            prompt_user_with_menu()
        # Deleting the book as per user wish
        elif add_or_not == 'x' or add_or_not == 'X':
            del collection[id]
    except Exception as error:
        print("Error: ", error)

def display_collection(collection):
    try:
        # Priming a counter outside for loop to keep track of the number items printed.
        count = 0
        # Function to print items based on user input.
        for id in collection:
            result = '\n'.join(f'{key}: {value}' for key, value in collection[id].items())
            print('\n', result, sep='')
            count += 1
            if count%10 == 0:
                # Asking user input '' for continuing and m to got to menu.
                next_ten = input("\nPress enter to show more items, or type 'm' to return to the menu: ")
                if next_ten == '':
                    continue
                elif next_ten == 'm':
                    prompt_user_with_menu()
            # Printing the last few items left.
            elif len(collection[id]) - count < 0:
                continue

    except Exception as error:
        print("Error: ", error)

def query_collection(collection):
    try:
        # Taking user input for the string to search.
        substring_to_find = str(input("Enter a query string to use for the search: "))
        for id in collection:
            # Searching the books dict using id.
            if 'Publisher' in collection[id]:
                # Checking for books with the string using lower function.
                if (substring_to_find.lower() in collection[id]['Title'].lower() or substring_to_find.lower() in collection[id]['Author'].lower() or substring_to_find.lower() in collection[id]['Publisher'].lower()):
                    result = '\n'.join(f'{key}: {value}' for key, value in collection[id].items())
                    print('\n', result, sep='')
            # Searching the movies dict using id.
            if 'Genre' in collection[id]:
                # Checking for movies with the string using lower function.
                if substring_to_find.lower() in collection[id]['Title'].lower() or substring_to_find.lower() in collection[id]['Director'].lower() or substring_to_find.lower() in collection[id]['Genre'].lower():
                        result = '\n'.join(f'{key}: {value}' for key, value in collection[id].items())
                        print('\n', result, sep='')
    except Exception as error:
        print("Error: ", error)

# This is the main program function.  It runs the main loop which prompts the user and performs the requested actions.
def main():
    # Load the collections, and check for an error.
    library_collections, max_existing_id = load_collections()

    if library_collections is None:
        print("The collections could not be loaded. Exiting.")
        return
    print("The collections have loaded successfully.")

    # Display the error and get the operation code entered by the user.  We perform this continuously until the
    # user enters "x" to exit the program.  Calls the appropriate function that corresponds to the requested operation.
    operation = prompt_user_with_menu()
    while operation != "x":
         if operation == "ci":
             check_in(library_collections)
         elif operation == "co":
             check_out(library_collections)
         elif operation == "ab":
             max_existing_id = add_book(library_collections["books"], max_existing_id)
         elif operation == "am":
             max_existing_id = add_movie(library_collections["movies"], max_existing_id)
         elif operation == "db":
             display_collection(library_collections["books"])
         elif operation == "dm":
             display_collection(library_collections["movies"])
         elif operation == "qb":
             query_collection(library_collections["books"])
         elif operation == "qm":
             query_collection(library_collections["movies"])
         else:
             print("Unknown command.  Please try again.")

         operation = prompt_user_with_menu()


# Kick off the execution of the program.
main()
