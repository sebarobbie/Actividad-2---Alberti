import string

class AlbertiCipher:
    def __init__(self, initial_letter='a', key_sequence=None):
        self.outer_ring = string.ascii_uppercase  # Alfabeto externo (estático)
        self.inner_ring_base = string.ascii_lowercase  # Alfabeto interno (rotativo)
        self.set_inner_ring(initial_letter)
        self.key_sequence = key_sequence or []

    def set_inner_ring(self, letter):
        """Gira el disco interno para que empiece desde 'letter'."""
        if letter not in self.inner_ring_base:
            raise ValueError("El carácter inicial debe estar entre a-z.")
        idx = self.inner_ring_base.index(letter)
        self.inner_ring = self.inner_ring_base[idx:] + self.inner_ring_base[:idx]

    def encrypt(self, message):
        result = ''
        key_index = 0

        for char in message:
            if char.upper() in self.outer_ring:
                idx = self.outer_ring.index(char.upper())
                result += self.inner_ring[idx]
                if self.key_sequence:
                    self.set_inner_ring(self.key_sequence[key_index % len(self.key_sequence)])
                    key_index += 1
            else:
                result += char  # Deja espacios y símbolos sin modificar
        return result

    def decrypt(self, message):
        result = ''
        key_index = 0

        for char in message:
            if char in self.inner_ring:
                idx = self.inner_ring.index(char)
                result += self.outer_ring[idx]
                if self.key_sequence:
                    self.set_inner_ring(self.key_sequence[key_index % len(self.key_sequence)])
                    key_index += 1
            else:
                result += char
        return result

# --- PROGRAMA PRINCIPAL ---
if __name__ == "__main__":
    print("\n=== Cifrado de Alberti ===")

    texto_original = input(" Ingresa el mensaje a cifrar: ").upper()
    letra_inicial = input(" Letra inicial del disco (a-z): ").lower()
    secuencia_clave = input(" Clave de cambios (ej: ekm), o dejar en blanco: ").lower()

    cambios = list(secuencia_clave) if secuencia_clave else []

    cifrador = AlbertiCipher(initial_letter=letra_inicial, key_sequence=cambios)

    texto_cifrado = cifrador.encrypt(texto_original)
    print("\n Texto cifrado:", texto_cifrado)

    # Para descifrar
    cifrador = AlbertiCipher(initial_letter=letra_inicial, key_sequence=cambios)
    texto_descifrado = cifrador.decrypt(texto_cifrado)
    print(" Texto descifrado:", texto_descifrado)

    input("\nPresiona Enter para salir...")
