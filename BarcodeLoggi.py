
class BarCodeLoggi:
    def __init__(self, *args) -> None:
        if len(args) == 2:
            self.ByPackBarcode(*args)
        if len(args) == 5:
            self.ByPackAttrs(*args)

    def ByPackBarcode(self, barcode_: str, n_pack_: int) -> None:
        self.barcode = barcode_
        barcode_ = barcode_.replace(" ", "")
        self.origin = barcode_[0:3]
        self.destiny = barcode_[3:6]
        self.loggi_code = barcode_[6:9]
        self.seller_code = barcode_[9:12]
        self.product_type = barcode_[12:15]
        self.n_pack = n_pack_

    def ByPackAttrs(self, origin_: str, destiny_: str, loggi_code_: str, seller_code_: str, product_type_: str, n_pack_: int) -> None:
        self.origin = origin_
        self.destiny = destiny_
        self.loggi_code = loggi_code_
        self.seller_code = seller_code_
        self.product_type = product_type_
        self.n_pack = n_pack_
        self.barcode = " ".join(
            [origin_, destiny_, loggi_code_, seller_code_, product_type_])

    def convertRegCodes(self, cod: str) -> str:
        regs_interval_codes = {"Centro-Oeste": (201, 299), "Nordeste": (
            300, 399), "Norte": (400, 499), "Sudoeste": (1, 99), "Sul": (100, 199)}
        for reg in regs_interval_codes.keys():
            if(int(cod) >= regs_interval_codes[reg][0] and int(cod) <= regs_interval_codes[reg][1]):
                return reg
        return "Região Inválida"

    def getOrigin(self) -> tuple:

        return (self.origin, self.convertRegCodes(self.origin))

    def getDestiny(self) -> tuple:
        return (self.destiny, self.convertRegCodes(self.destiny))

    def getLoggiCode(self) -> str:
        return self.loggi_code

    def getSellerCode(self) -> str:
        return self.seller_code

    def getProductType(self) -> tuple:
        prod_codes = {"001": "Jóias", "111": "Livros",
                      "333": "Eletrônicos", "555": "Bebidas", "888": "Brinquedos"}

        if self.product_type not in prod_codes.keys():
            return (self.product_type, "Invalid Product")
        return (self.product_type, prod_codes[self.product_type])

    def getBarcode(self) -> str:
        return self.barcode

    def getNPack(self) -> int:
        return self.n_pack

    def toString(self) -> str:
        return "Código: {barcode}\n" \
            "Região de origem:Cidade {origin_code}, região {origin_reg}\n" \
            "Região de destino:Cidade {destiny_code}, região {destiny_reg}\n" \
            "Código Loggi: {loggi_code}\n" \
            "Código do vendedor do produto: {seller_code}\n" \
            "Tipo do produto: {product_type}".format(barcode=self.getBarcode(), origin_code=self.getOrigin()[0], origin_reg=self.getOrigin()[1], destiny_code=self.getDestiny()[0], destiny_reg=self.getDestiny()[1],
                                                     loggi_code=self.getLoggiCode(), seller_code=self.getSellerCode(), product_type=self.getProductType())

    def isValid(self) -> bool:
        return not(self.getProductType()[1] == "Invalid Product" or (self.getProductType()[1] == "Jóias" and self.getOrigin()[1] == "Centro-Oeste") or self.getSellerCode() == "367" or (self.getOrigin()[1] == "Região Inválida" or self.getDestiny()[1] == "Região Inválida"))
