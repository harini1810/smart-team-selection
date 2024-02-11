from bardapi import Bard
import os
# from dotenv import load_dotenv

# load_dotenv()
token ="dQjabelo-G6Lk_t-kQTErqoAM3hXgJBvmT1h9iELekqEHlg1bnklN62fAJNd5bXNULKbmA."

bard = Bard(token = token)

# # while True:
# #     print()
# #     a = str(input("Ask Anything:"))
# #     print()
# #     print()
# #     if a == "thanks":
# #         break
# #     result = bard.get_answer(a)
# #     print(result['content'])


def chat(text) :
     return bard.get_answer(text)['content']