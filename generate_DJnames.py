
# While the sng package is not installed, add the package's path
# (the parent directory) to the library path:

import os
import sys
sys.path.insert(0, os.path.abspath('../../'))

import sng

cfg = sng.Config(
    epochs=50,
    min_word_len=2,
    max_word_len=8
)
print (cfg.to_dict())

# print (sng.show_builtin_wordlists())

artist_name = sng.load_builtin_wordlist('artist_name.txt')
# print (latin[:5])

gen = sng.Generator(wordlist=artist_name, config=cfg)
gen.fit()
print (gen.simulate(n=40))
gen.save('my_model.pkl', overwrite=True)
