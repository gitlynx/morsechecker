#
# Morse table in dits
#
from bitstring import Bits, BitArray

class Morse():
    dit = '10'
    dah = '1110'
    morse_a = BitArray(bin=dit + dah)
    morse_b = BitArray(bin=dah + dit + dit + dit)
    morse_c = BitArray(bin=dah + dit + dah + dit)
    morse_d = BitArray(bin=dah + dit + dit)
    morse_e = BitArray(bin=dit)
    morse_f = BitArray(bin=dit + dit + dah + dit)
    morse_g = BitArray(bin=dah + dah + dit)
    morse_h = BitArray(bin=dit + dit + dit + dit)
    morse_i = BitArray(bin=dit + dit)
    morse_j = BitArray(bin=dit + dah + dah + dah)
    morse_k = BitArray(bin=dah + dit + dah)
    morse_l = BitArray(bin=dit + dah + dit + dit)
    morse_m = BitArray(bin=dah + dah)
    morse_n = BitArray(bin=dah + dit)
    morse_o = BitArray(bin=dah + dah + dah)
    morse_p = BitArray(bin=dit + dah + dah + dit)
    morse_q = BitArray(bin=dah + dah + dit + dah)
    morse_r = BitArray(bin=dit + dah + dit)
    morse_s = BitArray(bin=dit + dit + dit)
    morse_t = BitArray(bin=dah)
    morse_u = BitArray(bin=dit + dit + dah)
    morse_v = BitArray(bin=dit + dit + dit + dah)
    morse_w = BitArray(bin=dit + dah + dah)
    morse_x = BitArray(bin=dah + dit + dit + dah)
    morse_y = BitArray(bin=dah + dit + dah + dah)
    morse_z = BitArray(bin=dah + dah + dit + dit)

    morse_1 = BitArray(bin=dit + dah + dah + dah + dah)
    morse_2 = BitArray(bin=dit + dit + dah + dah + dah)
    morse_3 = BitArray(bin=dit + dit + dit + dah + dah)
    morse_4 = BitArray(bin=dit + dit + dit + dit + dah)
    morse_5 = BitArray(bin=dit + dit + dit + dit + dit)
    morse_6 = BitArray(bin=dah + dit + dit + dit + dit)
    morse_7 = BitArray(bin=dah + dah + dit + dit + dit)
    morse_8 = BitArray(bin=dah + dah + dah + dit + dit)
    morse_9 = BitArray(bin=dah + dah + dah + dah + dit)
    morse_0 = BitArray(bin=dah + dah + dah + dah + dah)

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
