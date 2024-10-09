
<img src="images/octopusUNO.jpg" width="300" alt="octopusUNO">

# Github Search
 
 A simple application for discover developers and their own repositories in github. Show the repositories , stars, followers and following. 

## Prerequisites

- Python 3.8 or higher
- Remember your github token and/or to set in your environment variables in the following variable:
  - GITHUB_TOKEN    
The github token can be generated in the following link:
[Github Token](https://github.com/settings/tokens) and set in your environment variables.

================================================================================================================

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dynamic GitHub Page</title>
    <style>
        body { font-family: Arial, sans-serif; line-height: 1.6; padding: 20px; max-width: 800px; margin: 0 auto; }
        #result { margin-top: 20px; padding: 10px; border: 1px solid #ddd; }
    </style>
</head>
<body>
    <h1>My Dynamic GitHub Page</h1>
    <button onclick="runProgram()">Run Program</button>
    <div id="result"></div>

    <script>
        async function runProgram() {
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = 'Loading...';
            try {
                const response = await fetch('https://your-backend-url.com/run');
                const data = await response.json();
                resultDiv.innerHTML = `Result: ${data.output}`;
            } catch (error) {
                resultDiv.innerHTML = `Error: ${error.message}`;
            }
        }
    </script>
</body>
</html>
