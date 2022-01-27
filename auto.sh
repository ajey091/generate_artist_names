source ~/.bashrc
python post_process_artists.py
cat DJnames.txt >> artist_name.txt
cp artist_name.txt startup-name-generator/sng/wordlists/
cd startup-name-generator
python setup.py install
cd ..
python generate_DJnames.py
