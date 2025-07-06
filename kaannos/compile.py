import os
import key_compiler

this_dir = os.path.dirname(os.path.abspath(__file__))

locales = os.path.join(this_dir, "..", "locales")
output_path = os.path.join(this_dir, "..", "locales", "keys.py")

key_compiler.build_result(
    primary_lang="en",
    locale_dir=locales,
    output_path=output_path,
    types=True 
)