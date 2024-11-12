def decrypt_cypher_text(encrypted_text, key):
    # function implementation here...
    decrypted_text = ""
    for character in encrypted_text:
        ascii_value = ord(character)
        letter = chr((ascii_value - key) % 256)
        decrypted_text += letter
    return decrypted_text

print(decrypt_cypher_text("Hdfk#huuru#|rx#pdnh#lq#surjudpplqj#lv#dq#rssruwxqlw|#wr#ehfrph#d#ehwwhu#ghyhorshu$", 3))
#Returns "Each error you make in programming is an opportunity to become a better developer!"