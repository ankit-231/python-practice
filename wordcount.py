total_words = 17711
total_chunks = 19
average_words_in_each_chunk = total_words / total_chunks

# word_count_in_each_chunk = [
#     992,
#     952,
#     954,
#     985,
#     956,
#     992,
#     968,
#     932,
#     958,
#     973,
#     927,
#     900,
#     994,
#     951,
#     977,
#     976,
#     993,
#     954,
#     368,
# ]

# percentages = [
#     0.02,
#     0.02,
#     0.02,
#     0.05,
#     0.02,
#     0.05,
#     0.21,
#     0.02,
#     0.02,
#     0.02,
#     0.02,
#     0.02,
#     0.02,
#     0.03,
#     0.04,
#     0.02,
#     0.02,
#     0.02,
#     0.02,
# ]
word_count_in_each_chunk = [
    7512,
    7181,
    2893,
]

percentages = [
    0.26,
    0.36,
    0.5,
]


def calulate_overall(word_count_in_each_chunk, percentages):
    # Calculate the total AI words
    total_ai_words = sum(
        wc * ai for wc, ai in zip(word_count_in_each_chunk, percentages)
    )
    a = [wc * ai for wc, ai in zip(word_count_in_each_chunk, percentages)]
    print(a)
    print(total_ai_words)

    # Calculate the total word count
    total_word_count = sum(word_count_in_each_chunk)

    # Calculate the overall AI percentage
    overall_ai_percentage = (total_ai_words / total_word_count) * 100
    return overall_ai_percentage


overall_ai_percentage = calulate_overall(word_count_in_each_chunk, percentages)


print(f"Overall Plag Percentage: {overall_ai_percentage:.2f}%")
