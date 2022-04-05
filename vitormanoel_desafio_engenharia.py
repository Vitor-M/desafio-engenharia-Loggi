from struct import pack
import BarcodeLoggi


def main():
    packages = [
        "288355555123888",
        "335333555584333",
        "223343555124001",
        "002111555874555",
        "111188555654777",
        "111333555123333",
        "432055555123888",
        "079333555584333",
        "155333555124001",
        "333188555584333",
        "555288555123001",
        "111388555123555",
        "288000555367333",
        "066311555874001",
        "110333555123555",
        "333488555584333",
        "455448555123001",
        "022388555123555",
        "432044555845333",
        "034311555874001"]

    barcodes = list()
    for pack_index, barcode in enumerate(packages):
        barcodes.append(BarcodeLoggi.BarCodeLoggi(barcode, pack_index+1))

    # Question1(barcodes)
    # Question2(barcodes)
    # Question3(barcodes)
    # Question4(barcodes)
    # Question5(barcodes)
    # Question6(barcodes)
    # Question7(barcodes)
    # Question8(barcodes)
    # Question9(barcodes)
    # Question10(barcodes)


def Question1(barcodes):
    '''
    Identificar a região de destino de cada pacote, com totalização de pacotes (soma região);
    '''
    packs_byReg = {"Centro-Oeste": 0, "Nordeste": 0,
                   "Norte": 0, "Sudoeste": 0, "Sul": 0, "Região Inválida": 0}
    for barcode in barcodes:
        print("Pacote {n_pack}: {pack} Região: {region}".format(n_pack=barcode.getNPack(),
                                                                pack=barcode.getBarcode(), region=barcode.getDestiny()[1]))
        packs_byReg[barcode.getDestiny()[1]] += 1

    print("\nTotal de pacotes por região:")
    for region, n_packs in packs_byReg.items():
        print("Região: {region_}, Total de pacotes:{n_packs_}".format(
            region_=region, n_packs_=n_packs))


def Question2(barcodes):
    '''
    Saber quais pacotes possuem códigos de barras válidos e/ou inválidos;
    '''
    for barcode in barcodes:
        if(barcode.isValid()):
            print("Pacote {n_pack}: {pack}, Possui código de barras VÁLIDO".format(n_pack=barcode.getNPack(),
                                                                                   pack=barcode.getBarcode()))
        else:
            print("Pacote {n_pack}: {pack}, Possui código de barras INVÁLIDO".format(n_pack=barcode.getNPack(),
                                                                                     pack=barcode.getBarcode()))


def Question3(barcodes):
    '''
    Identificar os pacotes que têm como origem a região Sul e Brinquedos em seu conteúdo;
    '''
    south_toys = 0
    for barcode in barcodes:
        if(barcode.getOrigin()[1] == "Sul" and barcode.getProductType()[1] == "Brinquedos"):
            south_toys += 1
            print("Pacote {n_pack}: {pack}".format(n_pack=barcode.getNPack(),
                                                   pack=barcode.format(barcode.getBarcode())))

    if (south_toys == 0):
        print(
            "Não existem pacotes com origem na Região Sul cujo tipo de produto é Brinquedo")


def Question4(barcodes):
    '''
    Listar os pacotes agrupados por região de destino (Considere apenas pacotes válidos);
    '''
    packs_byReg = {"Centro-Oeste": [], "Nordeste": [],
                   "Norte": [], "Sudoeste": [], "Sul": []}
    for barcode in barcodes:
        if(barcode.isValid()):
            packs_byReg[barcode.getDestiny()[1]].append(barcode)

    print("Pacotes por região de destino:")
    for region, packs in packs_byReg.items():
        print("Região: {region_}".format(region_=region))
        for pack in packs:
            print("Pacote {n_pack}: {pack_}".format(
                n_pack=pack.getNPack(), pack_=pack.getBarcode()))
        print("\n")


def Question5(barcodes):
    '''
    Listar o número de pacotes enviados por cada vendedor (Considere apenas pacotes válidos);
    '''
    packs_bySeller = {}
    for barcode in barcodes:
        if(barcode.isValid()):
            if(barcode.getSellerCode() not in packs_bySeller.keys()):
                packs_bySeller[barcode.getSellerCode()] = [barcode]
            else:
                packs_bySeller[barcode.getSellerCode()].append(barcode)

    print("Pacotes por Vendedor:")
    for seller, packs in packs_bySeller.items():
        print("Código do vendedor do produto:: {seller_}".format(
            seller_=seller))
        for pack in packs:
            print("Pacote {n_pack}: {pack_}".format(
                n_pack=pack.getNPack(), pack_=pack.getBarcode()))
        print("\n")


def Question6(barcodes):
    '''
    Gerar o relatório/lista de pacotes por destino e por tipo (Considere apenas pacotes válidos);
    '''
    packs_byReg = {"Centro-Oeste": [], "Nordeste": [],
                   "Norte": [], "Sudoeste": [], "Sul": []}
    for barcode in barcodes:
        if(barcode.isValid()):
            packs_byReg[barcode.getDestiny()[1]].append(barcode)

    print("Pacotes por região de destino:")
    for region, packs in packs_byReg.items():
        print("Região: {region_}".format(region_=region))
        for pack in sorted(packs, key=lambda barcode: barcode.getProductType(), reverse=True):
            print("Tipo do produto: {product_type}, Pacote {n_pack}: {pack_}".format(
                product_type=pack.getProductType()[1], n_pack=pack.getNPack(), pack_=pack.getBarcode()))
        print("\n")


def Question7(barcodes):
    '''
    Se o transporte dos pacotes para o Norte passa pela Região Centro-Oeste, quais são os pacotes que devem ser despachados no mesmo caminhão?
    '''
    packs_byReg = {"Centro-Oeste": [], "Nordeste": [],
                   "Norte": []}
    print("Pacotes despachados no caminhão de rota Centro-Oeste -> Norte:")
    for barcode in barcodes:
        if(barcode.getDestiny()[1] in packs_byReg.keys()):
            print("Pacote {n_pack}: {pack_}".format(
                n_pack=barcode.getNPack(), pack_=barcode.getBarcode()))


def Question8(barcodes):
    '''
    Se todos os pacotes fossem uma fila qual seria a ordem de carga para o Norte no caminhão para descarregar os pacotes da Região Centro Oeste primeiro;
    '''
    packs_byReg = {"Norte": [], "Nordeste": [], "Centro-Oeste": []}
    print("Pacotes despachados no caminhão de rota Centro-Oeste -> Norte:")
    for barcode in barcodes:
        if(barcode.getDestiny()[1] in packs_byReg.keys()):
            packs_byReg[barcode.getDestiny()[1]].append(barcode)

    for packs in packs_byReg.values():
        for pack in packs:
            print("Pacote {n_pack}: {pack_}".format(
                n_pack=pack.getNPack(), pack_=pack.getBarcode()))


def Question9(barcodes):
    '''
    No item acima considerar que as jóias fossem sempre as primeiras a serem descarregadas;
    '''
    packs_byReg = {"Norte": [], "Nordeste": [], "Centro-Oeste": []}
    print("Pacotes despachados no caminhão de rota Centro-Oeste -> Norte:")
    for barcode in barcodes:
        if(barcode.getDestiny()[1] in packs_byReg.keys()):
            packs_byReg[barcode.getDestiny()[1]].append(barcode)

    for region, packs in packs_byReg.items():
        packs_byProd = []
        for pack in packs:
            if(pack.getProductType()[1] == "Jóias"):
                packs_byProd.insert(0, pack)
            else:
                packs_byProd.append(pack)
        packs_byReg[region] = reversed(packs_byProd)

    for packs in packs_byReg.values():
        for pack in packs:
            print("Pacote {n_pack}: {pack_}".format(
                n_pack=pack.getNPack(), pack_=pack.getBarcode()))


def Question10(barcodes):
    '''
    Listar os pacotes inválidos.
    '''
    for barcode in barcodes:
        if not barcode.isValid():
            print("Pacote {n_pack}: {pack_}".format(
                n_pack=barcode.getNPack(), pack_=barcode.getBarcode()))


main()
