from flask import Flask, render_template, request
app = Flask(__name__)

# ********* Index Page *********
@app.route("/")
def home():
    return render_template("index.html")

# ****************** Feature 2 ******************

# ********* Needed Functions *********
# ********* Encryption *********
def str2bin(secret_message):
    """Formats secret message into a list of characters as binary strings
    Args: 
    secret_message: str
    Returns: 
    secret_message: str ==> a str of characters as binary strings
    """
    bin_list = []
    for index, i in enumerate(secret_message):
        ascii_value = ord(i)
        temp = bin(ascii_value)[2:]
        temp_val = len(temp)
        if temp_val != 7:
            for x in range(7 - temp_val): temp = '0' + temp
        # adding space b/w each binary form of characters
        if index != len(secret_message) - 1: temp += " "
        bin_list.append(temp)
    return ''.join(bin_list)

def bin2hidden(secret_message):
    """Convert str of secert_message into a string of zero-width characters
    Args: 
    secret_message: str
    Returns: 
    secret_message: str ==> a secret_message string after replacing 0's, 1's and spaces with zero-width-characters
    """
    temp = ""
    for i in secret_message:
        if i == ' ':
            temp += '\u2060'
        if i == '0':
            temp += '\u200B'
        if i == '1':
            temp += '\u200C'
    return temp

def wrap(secret_message):
    """Wraps/Adds boundaries at start & end
    Args: 
    secret_message: str
    Returns: 
    secret_message: str ==> public message with hidden secret message in it
    """
    return "\uFEFF" + secret_message + "\uFEFF"



# ********* Decryption *********
def unwrap(hidden_public_message):
    """Unwraps/Removes boundaries at start & end
    Args: 
    hidden_public_message: str
    Returns: 
    hidden_public_message: str ==> unwrapped message
    """
    temp = hidden_public_message.split('\uFEFF')
    if len(temp) == 1:
        return False
    else:
        return temp[1]

def hidden2bin(unwrapped):
    """Convert str of unwrapped into a string of binary representation of each character of secret_message seperated by a space
    Args: 
    unwrapped: str
    Returns: 
    temp: str ==> each secret_message in its binary form seperated by a space
    """
    temp = ""
    for i in unwrapped:
        if i == '\u2060':
            temp += ' '
        if i == '\u200B':
            temp += '0'
        if i == '\u200C':
            temp += '1'
    return temp

def bin2str(unwrapped):
    """Converts binary form of each character to form secret_message
    Args: 
    unwrapped: str
    Returns: 
    temp: str ==> a str which is the secret_message
    """
    temp = ""
    char_list = unwrapped.split(" ")
    for i in char_list:
        temp += chr(int(i, 2))
    return temp


@app.route("/zeroWidthStego", methods=['GET', 'POST'])
def zero_width_stego():
    if request.method == 'GET':
        return render_template("zeroWidthStego.html")
    
    if request.method == 'POST':
        # to konw which form was submitted
        form_type = request.form.get('form_type')

        if form_type == 'left_form':
            public_message = str(request.form.get('inputPublicMsg'))
            secret_message = str(request.form.get('inputSecretMsg'))
            # ********* "Hide It" code here/Encryption code *********
            # finding half-way point
            half = round(len(public_message) / 2)
            # gets str2bin list & store it
            secret_message = str2bin(secret_message)
            # gets bin2hidden string & store it
            secret_message = bin2hidden(secret_message)
            # gets wrapped secret_message & store it
            secret_message = wrap(secret_message)
            # Inject secret_message at half index of public_message
            hidden_public_message = public_message[:half + 1] + secret_message + public_message[half + 1:]
            return render_template("zeroWidthStego.html", hidden_public_message=hidden_public_message)
        else:
            # below "Reveal It" variable
            hidden_public_message1 = str(request.form.get('inputPublicMsg1'))
            # ********* "Reveal It" code here/Decryption code *********
            # removes start & end boundaries
            unwrapped = unwrap(hidden_public_message1)
            toast_message = ""
            if not unwrapped:
                unwrapped = "NOTE: No private message was found in this public message. This is not a secret message."
                toast_message = "No secret message was found"
            else:
                # binary form of characters of secret_message
                unwrapped = hidden2bin(unwrapped)

                # gets secret_message
                unwrapped = bin2str(unwrapped)
                toast_message = ""  # Empty string if there is a private message

            return render_template("zeroWidthStego.html", unwrapped=unwrapped, toast_message=toast_message)





if __name__ == '__main__':
    app.run(debug=True, port=5001)