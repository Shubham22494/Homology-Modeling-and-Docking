def replace_letter(sequence, position, new_letter):
    """
    Replace a letter in the sequence at the specified position.

    :param sequence: The original sequence (string)
    :param position: The 1-based index where the replacement should occur
    :param new_letter: The new letter to replace at the specified position
    :return: Modified sequence with the replaced letter
    """
    if position < 1 or position > len(sequence):
        raise ValueError("Position out of range")

    # Convert to 0-based index
    position -= 1

    # Replace the character
    modified_sequence = sequence[:position] + new_letter + sequence[position + 1:]
    return modified_sequence



sequence = """MVRLPLQCVLWGCLLTAVHPEPPTACREKQYLINSQCCSLCQPGQKLVSDCTEFTETECL
PCGESEFLDTWNRETHCHQHKYCDPNLGLRVQQKGTSETDTICTCEEGWHCTSEACESCV
LHRSCSPGFGVKQIATGVSDTICEPCPVGFFSNVSSAFEKCHPWTSCETKDLVVQQAGTN
KTDVVCGPQDRLRALVVIPIIFGILFAILLVLVFIKKVAKKPTNKAPHPKQEPQEINFPD
DLPGSNTAAPVQETLHGCQPVTQEDGKESRISVQERQ*"""

# Remove newlines for a clean sequence
sequence = sequence.replace("\n", "")

# Example: Replace the 10th letter with 'X'
modified_seq = replace_letter(sequence, 227, 'A')
print(modified_seq)
