echo "Enter file path: "
read File
if [ -e "$File" ]; then
  echo "File exists."
else
  echo "File does not exist."
fi