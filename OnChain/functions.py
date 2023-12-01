def add_unit_to_bignumber(bignumber):

        bignumber = float(bignumber)
        units = ["", "K", "M", "B", "T", "Q", "Qi", "Sx", "Sp", "O", "N", "D"]
        unit_index = 0

        while bignumber >= 1000:
                bignumber /= 1000.0
                unit_index += 1

        formatted_number = "{:.2f}{}".format(bignumber, units[unit_index])
        return formatted_number