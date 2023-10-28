#! /bin/zsh

echo $1;
echo 'export OPENAI_API_KEY=$1' >> ~/.zshenv;
source ~/.zshenv;

exit 0;