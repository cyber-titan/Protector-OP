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


@app.route("/zero-width-stego", methods=['GET', 'POST'])
def zero_width_stego():
    if request.method == 'GET':
        return render_template("zero-width-stego.html")
    
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
            return render_template("zero-width-stego.html", hidden_public_message=hidden_public_message)
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

            return render_template("zero-width-stego.html", unwrapped=unwrapped, toast_message=toast_message)


# ****************** Feature 3 ******************
import random

@app.route('/strong-pass', methods=['GET', 'POST'])
def strong_pass_generator():
    if request.method == 'GET':
        return render_template("strong-pass.html")
    
    if request.method == 'POST':
        # STRONG PASSWORD GENERATOR

        """
        Len = 25 ==> abcdefghijklmnopqrstuvwxyz
        Len = 25 ==> ABCDEFGHIJKLMNOPQRSTUVWXYZ
        Len = 10 ==> 0123456789
        Len = 32 ==> !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ 
        """

        lower_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        upper_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~', '\\']

        # input size of password needed
        password_size = str(request.form.get('inputLengthOfPass'))
        temp = int(password_size)

        strong_password = []
        while temp > 0:
            if temp == 0: break
            # 1. choose a lower letter & shuffle result
            strong_password += random.choice(lower_letters)
            random.shuffle(strong_password)
            temp -= 1

            if temp == 0: break
            # 2. choose a upper letter & shuffle result
            strong_password += random.choice(upper_letters)
            random.shuffle(strong_password)
            temp -= 1

            if temp == 0: break
            # 3. choose a digit & shuffle result
            strong_password += random.choice(digits)
            random.shuffle(strong_password)
            temp -= 1

            if temp == 0: break
            # 4. choose a symbol & shuffle result
            strong_password += random.choice(symbols)
            random.shuffle(strong_password)
            temp -= 1

        strong_password = ''.join(strong_password)
        return render_template('strong-pass.html', strong_password=strong_password)


# ****************** Feature 4 ******************

@app.route('/pass-strength', methods=['GET', 'POST'])
def pass_strength():
    if request.method == 'GET':
        return render_template('pass-strength.html')

    if request.method == 'POST':
        # PASSWORD STRENGTH TESTER
        """
        Very Weak: Passwords that do not meet any of the specified criteria. ==> " "
        Weak: Passwords that meet only one or two of the specified criteria. ==> "HelloWorld"
        Moderate: Passwords that meet three of the specified criteria. ==> "HelloWorld1"
        Strong: Passwords that meet four of the specified criteria. ==> "HelloWorld12"
        Very Strong: Passwords that meet all of the specified criteria. ==> "HelloWorld12@"

        Len = 25 ==> abcdefghijklmnopqrstuvwxyz
        Len = 25 ==> ABCDEFGHIJKLMNOPQRSTUVWXYZ
        Len = 10 ==> 0123456789
        Len = 32 ==> !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ 
        """

        lower_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        upper_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~', '\\']

        lc, uc, dc, sc = 0, 0, 0, 0
        # take input
        password = request.form.get('inputPass')

        # go through whole password
        for i in password:
            if i.islower(): lc += 1
            if i.isupper(): uc += 1
            if i.isdigit(): dc += 1
            if i in symbols: sc += 1

        # calculate final score out of 5
        score = 0
        if len(password) >= 12: score += 1
        if lc: score += 1
        if uc: score += 1
        if dc: score += 1
        if sc: score += 1

        # output
        result = ""
        if score == 0: result = "Very Weak 😱"
        if score == 1 or score == 2: result = "Weak 😬"
        if score == 3: result = "Moderate 😐"
        if score == 4: result = "Strong 🙂"
        if score == 5: result = "Very Strong 😎"


        return render_template('pass-strength.html', result=result)

# ****************** Feature 1 ******************
@app.route('/', methods=['GET', 'POST'])
def 

if __name__ == '__main__':
    app.run(debug=True, port=5001)