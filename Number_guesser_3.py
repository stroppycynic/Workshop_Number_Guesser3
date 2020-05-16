from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def computer_guess():
    """Main function for our program."""
    if request.method == 'GET':
        return website1.format(1, 1000)
    else:
        min_number = int(request.form.get("min"))
        max_number = int(request.form.get("max"))
        user_answer = request.form.get("user_answer")
        guess = int(request.form.get("guess", 500))

        if user_answer == "Too big":
            max_number = guess
        elif user_answer == "Too small":
            min_number = guess
        elif user_answer == "You win":
            return website_winner.format(guess=guess)

        guess = (max_number - min_number) // 2 + min_number

        return website2.format(guess=guess, min=min_number, max=max_number)


website1 = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Guess The Number</title>
</head>
<body>
<p>Imagine random number from 1 to 1000 and I will try to guess it in max. 10 tries. </br>
If I guess the number that is smaller than your number, choose: "Too small".</br>
If I guess the number that is bigger than your number, choose: "Too big".</br>
If I guess correctly, choose: "You win" </p>
<form action="" method="POST">
    <input type="hidden" name="min" value="{}"></input>
    <input type="hidden" name="max" value="{}"></input>
    <input type="submit" value="OK">
</form>
</body>
</html>"""

website2 = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Guess The Number</title>
</head>
<body>
<h1>I'm guessing your number is: {guess}</h1>
<form action="" method="POST">
    <input type="submit" name="user_answer" value="Too big">
    <input type="submit" name="user_answer" value="Too small">
    <input type="submit" name="user_answer" value="You win">
    <input type="hidden" name="min" value="{min}">
    <input type="hidden" name="max" value="{max}">
    <input type="hidden" name="guess" value="{guess}">
</form>
</body>
</html>"""

website_winner = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Guess The Number</title>
</head>
<body>
<h1>Hurray! I guessed! Your number is {guess}</h1>
</body>
</html>"""


if __name__ == '__main__':
    app.run()