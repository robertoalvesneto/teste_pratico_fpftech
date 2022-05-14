mkdir roberto
cd roberto
mkdir resultado
curl -s "https://fonts.google.com/download?family=Roboto" --output Roboto.zip
mkdir Roboto
unzip -q Roboto.zip -d Roboto
mv Roboto resultado/
rm Roboto.zip
