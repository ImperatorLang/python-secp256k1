import ctypes


invalid_seckeys = [
    b"\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xfe\xba\xae\xdc\xe6\xafH\xa0;\xbf\xd2^\x8c\xd06AA",  # curve order
    b"\x00" * 32,  # null

]
invalid_seckey_length = [
    31 * b"\x00",  # too short
    33 * b"\x00",  # too long
]

invalid_pubkey_serialization_length = [
    # correct is 33 for compressed and 65 for uncompressed and hybrid
    b"\x01" * 32,
    b"\x01" * 34,
    b"\x01" * 64,
    b"\x01" * 66,
]

invalid_pubkey_length = [
    ctypes.create_string_buffer(63),  # too short
    ctypes.create_string_buffer(65),  # too long
]

invalid_signature_length = invalid_pubkey_length  # both must be 64 bytes

invalid_compact_sig_length = [
    63 * b"\x01",
    65 * b"\x01",
]

invalid_xonly_pubkey_length = invalid_seckey_length

invalid_keypair_length = [
    ctypes.create_string_buffer(95),  # too short
    ctypes.create_string_buffer(97),  # too long
]

invalid_recoverable_signature_length = [
    ctypes.create_string_buffer(64),  # too short
    ctypes.create_string_buffer(66),  # too long
]

invalid_rec_ids = [-1, 4, 5]

valid_seckeys = [
    b'\x97\xe0{\xd6\x7f\xe1\xc52(5\x81\xc9\xfeg_\x8d\x1b0\xecwv\x9a\xf5\xfd\xae\t\xf0y\xdc\x19Z\xde',
    b"\xd4\x8c\x88Q/\x15\xc6(\xc6\x11\xaeU\xd0\xb5`\x9b\xcfcZ1'\xec\x83S\x08\x82\x9c:\xce2\xdc\x81",
    b'\x1e\xfa\x14\xd7*\xdd\x84Me\xf6^p\xcek\xc0\xab\x1d\x07\xb5\xaa\xd9L\x01:\x91SS\x8dS\x0b\x1f\x87',
    b'\x9e\xd0\xac\xfcutu\xe5\xda\x87\x82X\xdby\x9bx\xf0\nM\xcc+R\x1fv\xaa\xa3[\xbd\xbfg\xd2\x10',
    b'\xf3\xf6\x8a;\xf1\x9a\xbd|\x8b-\x13/K/\xae\x86\xb4_>\xef\xca|\x96.\xfa\x05\xe2\xfe=\xc9\xa4\x16',
    b"T\x7f6\x1a\x17\xfaQ\x9b\xb3\x173U\xb0\xd9\xf88+A\xdbx\x17V'\x8apU\xab\xe5JN\x12\xa3",
    b'\x85\xc5\x0c\xe0/.\x08\x7fPlb\xfc\x98\x8d<\xf6\x06\x88]\x8cd\x8c\x8f46\xdc\x04\xa5\x17\x05[\x9b',
    b'e\xb0(`J\xaf\xab\x9aY\xcb\x1e\xd3\x05\xf2\x012\x83\xd4\xbdw\xca\xa9,\xe0\x9a{\xf2\x9d\x19\xdeJ\x81',
    b"`'f/9D25j\xb7\xe7\x8d\xcf\xfc5\xedy\xa7?\x8f\xc8/(\xd6\xf3!\xb8\r\x8e\xa5K\xed",
    b'\xa5#k\xae\x1c&.\xb1\xa9n\x7f\xcb\x08\xb8\x87&\t\x02T\x95\x04\x93\x1a\xfc\x1a\xce\xd5\x99\xbd\xbbBe',
    b'g-\x8d\x91\xe0,+u\x8b\xb6\x9fQ\x199Esa\x9f\x8c\xe6\xe5\xae.9o\xb1\x9e\xa3\xda#\xbc\x91',
    b'e\x89\x92\x13\xc7\xb6`k\x06^-\n\x87\xac\xd9!\x81\xdc\xaa5\x08.d\xb0\x1b\xfa\xa8\x1b\x1a\xe5WJ',
    b'JXI\x9e4a{\xa1\xb7\xbf%\xaa\xdf\x89L\x9d\x08\x85;,\x05\xb4\xae\x13\xd5e$[W\xf8#\x10',
]

serialized_pubkeys_compressed = [
    b'\x02\x1bY\xc0\xea\xa56Z\r\xbf\x1f8\xff\xc1\x1c\xb1\x9c1\xbe\x9a"\x92\xbd\xcb~\x8f\xb4-\xa3*[\x1e\x93',
    b'\x02\xf0\x08\xb4\xe5\xad\xe1#n\x97\xdc]=\x81\xea\xb7\xbe\x85S\xce\x88\xc5\x08\x1c\xba|\xe8\x11C\xd3\x05\x80)',
    b'\x03Bs\x01a\xce>\x8b\x9dzw\x7fK\x0f\x0cp\x1f5\x7f\xe5<\xbf\xa6p\xbc\xaf\n\xdb\xc4}}\xf7E',
    b'\x03s\xbd\xf7u\xa6\x972u\xb56\xbc\x8b\xad\x1e\\gq\xeaT\xa3J\x01\xa6\xaaY.dg[=\x0e\xf7',
    b'\x03\x99\x86}\xc5`n\xe0@\\\xcb\x89\x18\xdf5\xad\x02\xa1\xfbI\xa8\x81\x08t\x10\xf5#s\x8c\xff\x89c\xb1',
    b'\x03\x8b~\xde\x0b\xebG\xaf\xae\xaf!\xd6\xaf\xc4\x7f,\xadG\xf2<\xfe5\x08\x90\x85J\xd9\xf0}p\xe9\xf1*',
    b'\x03(k\x9f<\xf0h\xe7fU\x0cxf\xfd\xed!\x8d(\xcb\xbe\xd5g^rP/\xb7+\x83\xd7RL\x1e',
    b'\x02\xd5\xddTp\xdf2\xf1\x05L\x94\x04\xdd\xbc\x00\\=\xed\x95/\n\x9b^\x9e\x8f\xfbB.j\xa3\xa0\x97\xba',
    b'\x02 k\xfbO\xf5\x92FSTC\xe7Te\x1a\x0cn\x9cC\x82.\xe5\x94\xd4\xb2\x1e\xbc\x98\x07\x89\xb4\xea\xd3',
    b'\x03VE\x00\x9b:"\xc3\x89+\x17K^\xc7\xe8\x02\xa3@\x85P\x9b<\x8a\xabr\xa5\x9c\xe3>\xda\x9ex1',
    b'\x03;\xe5~\xe1_\xf5ym|\x7f\xe1\xc8\n\x7f\xe1\x17\xbe\x0f[c\x8bq}\x16\xc8G\x13\xebbe\xe9h',
    b'\x03\xf6\x98\xa7\xb6\x83\xc8\x02C"\xd0\x00/\x99f\r\x17\xa9b\xe8\x1b,\x88\xde3\x1f\x8a\xabSp\x93\xb0\xc2',
    b'\x02e\xd0\xf6*\xc5\xf9r\xd9Ah\\\xeb\x94*\x1c\x1fA\xfc\xeb\x904\r_\x8a\xee\xd6\xed\xdb\xb6\xd2\xec1',
]

serialized_pubkeys = [
    b'\x04\x1bY\xc0\xea\xa56Z\r\xbf\x1f8\xff\xc1\x1c\xb1\x9c1\xbe\x9a"\x92\xbd\xcb~\x8f\xb4-\xa3*[\x1e\x93Ry,/\x94]\x0f\xb5\xbc~\xd8\xb2\xfa`i\xe6\xc7\x042\xaa\x16\xd1G\x17GL(\xae\xd2\xdd&\xd8',
    b"\x04\xf0\x08\xb4\xe5\xad\xe1#n\x97\xdc]=\x81\xea\xb7\xbe\x85S\xce\x88\xc5\x08\x1c\xba|\xe8\x11C\xd3\x05\x80)'\xaa\xecy\x7f\xcdaH\xea\xe1\xff*\xcf\xc0\x01_\xdc\x0f|\x11\x0e,R\x9c\x17\xa5b\xb90&/\x8e",
    b'\x04Bs\x01a\xce>\x8b\x9dzw\x7fK\x0f\x0cp\x1f5\x7f\xe5<\xbf\xa6p\xbc\xaf\n\xdb\xc4}}\xf7Eq9n\x990\x14|\xa4j\xb5v\x81\x18w\xf0\xf1\xa3\xdd\xac\xf2\xf6F\x18$S$\xa2\xcf}l \x8f',
    b'\x04s\xbd\xf7u\xa6\x972u\xb56\xbc\x8b\xad\x1e\\gq\xeaT\xa3J\x01\xa6\xaaY.dg[=\x0e\xf7\x81\xc6gct\xc5\xf4\x04\x8c\xcd-*\x11\xf8\x82\xa9\x16\xb4\xeb\x92%\xe8O\xcf\xdc&\xe1"\xfdo\xb4\xbb',
    b"\x04\x99\x86}\xc5`n\xe0@\\\xcb\x89\x18\xdf5\xad\x02\xa1\xfbI\xa8\x81\x08t\x10\xf5#s\x8c\xff\x89c\xb1\x1b\xc7G\x05\xad\x9em\xc9$\xb9\xce\xacK\xd46\xc7\x9f\x98\x9d\x17]\xaf\xe7*\x82\x1b\x8a5\x80+'\x81",
    b'\x04\x8b~\xde\x0b\xebG\xaf\xae\xaf!\xd6\xaf\xc4\x7f,\xadG\xf2<\xfe5\x08\x90\x85J\xd9\xf0}p\xe9\xf1*\xe2\x185\x82\xb4\xe9t\x1f\xb1\x99\xecI\xe5p\x7f\xeb\xf9\x11<\x97\xf0\xfeV\x00\x11\x04\xd0\x01\x18g\xc1\x8d',
    b'\x04(k\x9f<\xf0h\xe7fU\x0cxf\xfd\xed!\x8d(\xcb\xbe\xd5g^rP/\xb7+\x83\xd7RL\x1eL\x1d\x04Av\xc2\xe9A\xd9Y3<\xa8\xf7y\xfcrw\x16\xa0\xfa\x01\xe7\xfe}\xc9\x1a\xfb\xd3\x93\xcc\xed',
    b'\x04\xd5\xddTp\xdf2\xf1\x05L\x94\x04\xdd\xbc\x00\\=\xed\x95/\n\x9b^\x9e\x8f\xfbB.j\xa3\xa0\x97\xba\xb8\xe5\x18\x90Y\xeb\x0b?\x19\xbe|\xd7\xb6\xe3\x0c\x99\x95\xb4#\xef\xc9u\xcd-,\xdb\xc3\xb5\xcb!\xb2\xb8',
    b'\x04 k\xfbO\xf5\x92FSTC\xe7Te\x1a\x0cn\x9cC\x82.\xe5\x94\xd4\xb2\x1e\xbc\x98\x07\x89\xb4\xea\xd3\xfa\x18\x02\xe4I$vek\xdc\xe7\xa5\xba.\xa9\xb2\xb8\xdd\xef\x8fx\xd9\x0e\xc7z\x9f6\xdah\xeb6~',
    b'\x04VE\x00\x9b:"\xc3\x89+\x17K^\xc7\xe8\x02\xa3@\x85P\x9b<\x8a\xabr\xa5\x9c\xe3>\xda\x9ex1er\x9ef\xa3\xaf\xd1\x05\xd7~\x18\x95j\xfa\x83\t\xb5\x85\x1c\x07\x02\\lQ\xe1{\xc2\x17\x94L\xe4\x87',
    b'\x04;\xe5~\xe1_\xf5ym|\x7f\xe1\xc8\n\x7f\xe1\x17\xbe\x0f[c\x8bq}\x16\xc8G\x13\xebbe\xe9h\x17A\x18\x19@\xbar\x14\x93<Zq\x8e~#\x13r\xbbl\xc18\xbb\x1dOeH\xf4\x92\xba\x15\xbf\x17',
    b'\x04\xf6\x98\xa7\xb6\x83\xc8\x02C"\xd0\x00/\x99f\r\x17\xa9b\xe8\x1b,\x88\xde3\x1f\x8a\xabSp\x93\xb0\xc2\x9d0m6$\x9f\x15\xfd\x9d\x89\xecD\xbd\xca\xaf\xf5:kp\x92\x04\xb2\xe2\xaa\x91\x02\xb3?ZaWA',
    b'\x04e\xd0\xf6*\xc5\xf9r\xd9Ah\\\xeb\x94*\x1c\x1fA\xfc\xeb\x904\r_\x8a\xee\xd6\xed\xdb\xb6\xd2\xec1\xae\x18!\xea)"\xdc\x1a\x9d\xa4\x08*\xce\x03\xe7\xb7%\x03\xfcQ\xb2c\xba\x90\x07\xa7|\xd8([\x10d',
]

valid_der_sig_serializations = [
    b'0D\x02 +{\x89\x95\r\\I\x0f(q\x9d\xf0B\xe2R\xeb\x11(\xc2\x87\x18\x9c-\x18da\x82+`"!I\x02 Q]\xe3N\xa4\x0b7V\x9dy\xdfAU\xf4;\x89OW\xdd\xf3)\xd9\xd3\xe9B\x0b\x0c\xe1\xc0Cq\xff'
]

valid_compact_sig_serializations = [
    b'\x1a#\x05\x1c\x02^\x9d\x0c\xf6\xbf\xdb7\x12 \x0e"8\x87\'8D\xc6\x1172\xc1\xc8\xab\xab\n\xf9\\Cl\x8fP\'\xc6\xd3\xc3\xdd\xbd3X\xdc\xc1\x87m\xa4\xa4e\x1d\x7f\x92\xd44J\xf2C\x03\xa7\x07\xf2]'
]

not_bytes = [
    None,
    48.12,
    [1, 2],
    {"seckey": b"\x00"},
    {1, 2, 3, 4, 5},
    (None, None, None),
    bytearray([20, 58]),
    78,
]
not_c_char_array = not_bytes + [b"\x01" * 32]
not_int = not_bytes[:-1] + [b"\x01" * 32]
not_bool = not_bytes + [b"\x01" * 32]
