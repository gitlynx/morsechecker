#
# Morse table in dits
#
# References:
#  https://pypi.org/project/bitstring/
#
from bitstring import Bits, BitArray

class Morse():
    dit = '10'
    dah = '1110'
    morse_a = Bits(bin=dit + dah)
    morse_b = Bits(bin=dah + dit + dit + dit)
    morse_c = Bits(bin=dah + dit + dah + dit)
    morse_d = Bits(bin=dah + dit + dit)
    morse_e = Bits(bin=dit)
    morse_f = Bits(bin=dit + dit + dah + dit)
    morse_g = Bits(bin=dah + dah + dit)
    morse_h = Bits(bin=dit + dit + dit + dit)
    morse_i = Bits(bin=dit + dit)
    morse_j = Bits(bin=dit + dah + dah + dah)
    morse_k = Bits(bin=dah + dit + dah)
    morse_l = Bits(bin=dit + dah + dit + dit)
    morse_m = Bits(bin=dah + dah)
    morse_n = Bits(bin=dah + dit)
    morse_o = Bits(bin=dah + dah + dah)
    morse_p = Bits(bin=dit + dah + dah + dit)
    morse_q = Bits(bin=dah + dah + dit + dah)
    morse_r = Bits(bin=dit + dah + dit)
    morse_s = Bits(bin=dit + dit + dit)
    morse_t = Bits(bin=dah)
    morse_u = Bits(bin=dit + dit + dah)
    morse_v = Bits(bin=dit + dit + dit + dah)
    morse_w = Bits(bin=dit + dah + dah)
    morse_x = Bits(bin=dah + dit + dit + dah)
    morse_y = Bits(bin=dah + dit + dah + dah)
    morse_z = Bits(bin=dah + dah + dit + dit)

    morse_1 = Bits(bin=dit + dah + dah + dah + dah)
    morse_2 = Bits(bin=dit + dit + dah + dah + dah)
    morse_3 = Bits(bin=dit + dit + dit + dah + dah)
    morse_4 = Bits(bin=dit + dit + dit + dit + dah)
    morse_5 = Bits(bin=dit + dit + dit + dit + dit)
    morse_6 = Bits(bin=dah + dit + dit + dit + dit)
    morse_7 = Bits(bin=dah + dah + dit + dit + dit)
    morse_8 = Bits(bin=dah + dah + dah + dit + dit)
    morse_9 = Bits(bin=dah + dah + dah + dah + dit)
    morse_0 = Bits(bin=dah + dah + dah + dah + dah)

    morse_dict = {
            'a' : morse_a,
            'b' : morse_b,
            'c' : morse_c,
            'd' : morse_d,
            'e' : morse_e,
            'f' : morse_f,
            'g' : morse_g,
            'h' : morse_h,
            'i' : morse_i,
            'j' : morse_j,
            'k' : morse_k,
            'l' : morse_l,
            'm' : morse_m,
            'n' : morse_n,
            'o' : morse_o,
            'p' : morse_p,
            'q' : morse_q,
            'r' : morse_r,
            's' : morse_s,
            't' : morse_t,
            'u' : morse_u,
            'v' : morse_v,
            'w' : morse_w,
            'x' : morse_x,
            'y' : morse_y,
            'z' : morse_z,
            '0' : morse_0,
            '1' : morse_1,
            '2' : morse_2,
            '3' : morse_3,
            '4' : morse_4,
            '5' : morse_5,
            '6' : morse_6,
            '7' : morse_7,
            '8' : morse_8,
            '9' : morse_9}



if __name__ == "__main__":
    import pdb
    pdb.set_trace()
    print("Something random")
