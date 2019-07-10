class TokenSplitter:
    def __init__(self):
        pass

    def get_min_length(self, sentence, dict):
        minimum_len = 0
        if len(sentence) > max(dict.keys()):
            minimum_len = max(dict.keys())
        else:
            minimum_len = len(sentence)

        return minimum_len

    def token_analyser(self, sentence, dict, en_fa):
        minimum_len = self.get_min_length(sentence, dict)
        new_tokens = ""

        while sentence:

            if sentence[:minimum_len] in dict.get(minimum_len, ''):
                new_tokens += sentence[:minimum_len] + " "
                sentence = sentence.replace(sentence[:minimum_len], '')
                minimum_len = self.get_min_length(sentence, dict)
            else:
                minimum_len -= 1
                if minimum_len == 0:
                    if not en_fa:
                        new_tokens = "Error"
                    else:
                        new_tokens = "خطا"
                    break

        return new_tokens

    def splite_english(self):
        token_array = []
        merged_token_array = []
        english_dict = dict()
        with open("en.tokens.en", "r", encoding="utf8") as en_tokens:
            token_array = en_tokens.read().splitlines()

        with open("mergedTokens.en", "r", encoding="utf8") as en_merged_tokens:
            merged_token_array = en_merged_tokens.read().splitlines()
        for splited_word in token_array:
            if len(splited_word) in english_dict:
                english_dict[len(splited_word)].append(splited_word)
            else:
                english_dict[len(splited_word)] = [splited_word]
        with open('output/english_splited_token.txt', 'w+') as english_output:
            for sentence in merged_token_array:
                english_output.write("{} : {} \n".format(sentence, self.token_analyser(sentence, english_dict, 0)))

    def splite_farsi(self):
        merged_token_array = []
        farsi_dict = dict()
        with open("fa.words.txt", "r", encoding="utf8") as fa_tokens:
            for line in fa_tokens:
                w = line.strip('\n').split('\t')[0]
                if len(w) in farsi_dict:
                    farsi_dict[len(w)].append(w)
                else:
                    farsi_dict[len(w)] = [w]

        with open("mergedTokens.fa", "r", encoding="utf8") as fa_merged_tokens:
            merged_token_array = fa_merged_tokens.read().splitlines()
        with open('output/farsi_splited_token.txt', 'w+', encoding="utf8") as farsi_output:
            for sentence in merged_token_array:
                farsi_output.write("{} :  {} \n".format(sentence, self.token_analyser(sentence, farsi_dict, 1)))

if __name__ == "__main__":
    sp = TokenSplitter()
    sp.splite_english()
    sp.splite_farsi()
