#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Standard library imports
import regex as re
import logging

# Third-party imports (install these with pip)
import MeCab


def vocab_from_texts(texts: list) -> set:
    vocab = dict()
    mecab = MeCab.Tagger()
    confirm_japanese_pattern = re.compile(r"[\p{IsHiragana}\p{IsKatakana}\p{IsHan}]+")
    katakana_only_pattern = re.compile(r"[\p{IsKatakana}]+")
    for text in texts:
        parsed = mecab.parse(text)
        words = parsed.split("\n")
        for word in words:
            word_info = word.split("\t")
            if word == "EOS" or word == "" or len(word_info) < 4:
                continue
            # The 1st element contains the word itself, while the 4th element contains the base form
            # For some reason the 4th element contains the english translation
            # for katakana-only words, so we differentiate between katakana-only
            # words and other words
            base_form = (
                word_info[0]
                if katakana_only_pattern.match(word_info[0])
                else word_info[3]
            )
            # Sometimes the base form is followed by a hyphen and more text about word type
            base_form = base_form.split("-")[0]
            if confirm_japanese_pattern.match(base_form):
                if base_form in vocab.keys():
                    vocab[base_form] += 1
                else:
                    vocab[base_form] = 1

    return vocab

with open("tokenizerinput.txt", "r", encoding="utf8") as f:
  vocab_dictionary = vocab_from_texts(f.read().split("\n"))

new_vocab_dictionary = dict()
for (k, v) in vocab_dictionary.items():
    if (v != 1):
      new_vocab_dictionary[k] = v
with open("finaltext.csv", "w", encoding="utf8") as f:
  for (k, v) in new_vocab_dictionary.items():
     f.write(k + "\t" + str(v) + "\n")