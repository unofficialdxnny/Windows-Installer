# Source URL
$url = 'https://bit.ly/3318e1R'

# Destation file
$dest = "./Windows 7"

# Download the file
Invoke-WebRequest -Uri $url -OutFile $dest