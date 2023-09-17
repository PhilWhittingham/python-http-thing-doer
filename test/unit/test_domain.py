


from app.domain import CharCounter


def test_char_counter_given_input_string_counts_characters():
    input_string = "this is our string"

    character_counter = CharCounter(input=input_string)
    charater_counts = character_counter.count_characters()

    t_counts = [character_count for character_count in charater_counts if character_count.char == "t"]
    assert len(t_counts) == 1
    assert t_counts[0].count == 2