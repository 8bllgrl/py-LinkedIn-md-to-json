import io
import csv


def makeArrayWithDoubleQuotes(my_array):
    # check if array is None
    if my_array is None:
        print("Error: array is None")
        return ""

    # create a string buffer to hold the output
    output = io.StringIO()

    # create a CSV writer with quotechar='"'
    writer = csv.writer(output, quoting=csv.QUOTE_ALL, quotechar='"')

    # write the array to the output buffer
    writer.writerow(my_array)

    # return the output buffer as a string
    return output.getvalue()
