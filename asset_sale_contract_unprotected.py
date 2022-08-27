from pyteal import *


def asset_sale_contract(seller: str, asset_index: int, price: int):
    # reproductive justice: 25%
    COLLAB_ORG_ADDRESS = '3A2GMSYRUVFLBK7F3IUA6XOBHYL3NLGIBJBB7CWW7F6TLEJXKY6RZOHMOU'

    # collaborating artists: 50% total
    COLLAB_1_ADDRESS = 'CDDY6HNSDADMNMINRAX5S4I6ZTM4NUI3ET44UMFZCGBWJ2HAEDG5LJDK5A'
    COLLAB_2_ADDRESS = 'WQDDG4ANZJLL657VWU2OBM54OQIXT7ZHRWD5CLPJMRXNRBUZSI3CS7KXSU'
    COLLAB_3_ADDRESS = 'EFI6V5ZARB7FI5N3HX3KMEMYYKXIVKGAEUQZ75PHQEFIBUK7XRMXHKW6FE'
    COLLAB_4_ADDRESS = 'NLRJEJT7H7OJ3ZJJ3ZONV3X33NP25WC4VIHYUQJQU26AJXENJJW4TV7IPQ'
    COLLAB_5_ADDRESS = 'JCFE3QFMLPOS4MWKZ7DV6MYH5JP4GXGREYQDXMFQA42HRQKDDHAJQ7ZBYU'
    COLLAB_6_ADDRESS = '57VDOQC7DNGTEAX6KSCPTPK6CRZIZMPP2XW63KV52X7ANIWAVOIJTDJ5XY'
    COLLAB_7_ADDRESS = 'SWP7ANEB4BM7KICPHNXLY25EM2N24PHZQUCDIJ5LW7PKB6P3XOW5UL7JMA'
    COLLAB_8_ADDRESS = 'EH433KSF5AYEWO7BERGUJUDMPLRVRNSYUCS62KLYPRBJ7672JC2ODBD5FY'

    put_on_sale = And(
        # fund escrow
        Gtxn[0].type_enum() == TxnType.Payment,
        Gtxn[0].amount() == Int(int(0.5 * 1e6)),
        Gtxn[0].sender() == Addr(seller),
        Gtxn[0].close_remainder_to() == Global.zero_address(),
        # opt in escrow
        Gtxn[1].type_enum() == TxnType.AssetTransfer,
        Gtxn[1].asset_amount() == Int(0),
        Gtxn[1].sender() == Gtxn[0].receiver(),
        Gtxn[1].sender() == Gtxn[1].asset_receiver(),
        Gtxn[1].asset_close_to() == Global.zero_address(),
        Gtxn[1].xfer_asset() == Int(asset_index),
        # transfer asset to escrow
        Gtxn[2].type_enum() == TxnType.AssetTransfer,
        Gtxn[2].asset_amount() == Int(1),
        Gtxn[2].sender() == Addr(seller),
        Gtxn[2].asset_receiver() == Gtxn[1].sender(),
        Gtxn[2].asset_close_to() == Global.zero_address(),
        Gtxn[2].xfer_asset() == Int(asset_index),
    )

    buy_asset = And(
        # pay seller 25% of the sale
        Gtxn[0].type_enum() == TxnType.Payment,
        Gtxn[0].amount() == Int(int(price * 250000)),
        Gtxn[0].receiver() == Addr(seller),
        Gtxn[0].close_remainder_to() == Global.zero_address(),
        # opt in buyer to nft
        Gtxn[1].type_enum() == TxnType.AssetTransfer,
        Gtxn[1].asset_amount() == Int(0),
        Gtxn[1].sender() == Gtxn[0].sender(),
        Gtxn[1].sender() == Gtxn[1].asset_receiver(),
        Gtxn[1].asset_close_to() == Global.zero_address(),
        Gtxn[1].xfer_asset() == Int(asset_index),
        # transfer asset to buyer
        Gtxn[2].type_enum() == TxnType.AssetTransfer,
        Gtxn[2].asset_amount() == Int(1),
        Gtxn[2].asset_receiver() == Gtxn[1].sender(),
        Gtxn[2].asset_close_to() == Gtxn[1].sender(),
        Gtxn[2].xfer_asset() == Int(asset_index),
        # close escrow remainder to seller
        Gtxn[3].type_enum() == TxnType.Payment,
        Gtxn[3].amount() == Int(0),
        Gtxn[3].receiver() == Addr(seller),
        Gtxn[3].close_remainder_to() == Addr(seller),
        Gtxn[3].sender() == Gtxn[2].sender(),
        # pay reproductive justice 25% of the sale
        Gtxn[4].type_enum() == TxnType.Payment,
        Gtxn[4].amount() == Int(int(price * 250000)),
        Gtxn[4].receiver() == Addr(COLLAB_ORG_ADDRESS),
        Gtxn[4].close_remainder_to() == Global.zero_address(),
        # pay collaborator 1 6.25% of the sale
        Gtxn[5].type_enum() == TxnType.Payment,
        Gtxn[5].amount() == Int(int(price * 62500)),
        Gtxn[5].receiver() == Addr(COLLAB_1_ADDRESS),
        Gtxn[5].close_remainder_to() == Global.zero_address(),
        # pay collaborator 2 6.25% of the sale
        Gtxn[6].type_enum() == TxnType.Payment,
        Gtxn[6].amount() == Int(int(price * 62500)),
        Gtxn[6].receiver() == Addr(COLLAB_2_ADDRESS),
        Gtxn[6].close_remainder_to() == Global.zero_address(),
        # pay collaborator 3 6.25% of the sale
        Gtxn[7].type_enum() == TxnType.Payment,
        Gtxn[7].amount() == Int(int(price * 62500)),
        Gtxn[7].receiver() == Addr(COLLAB_3_ADDRESS),
        Gtxn[7].close_remainder_to() == Global.zero_address(),
        # pay collaborator 4 6.25% of the sale
        Gtxn[8].type_enum() == TxnType.Payment,
        Gtxn[8].amount() == Int(int(price * 62500)),
        Gtxn[8].receiver() == Addr(COLLAB_4_ADDRESS),
        Gtxn[8].close_remainder_to() == Global.zero_address(),
        # pay collaborator 5 6.25% of the sale
        Gtxn[9].type_enum() == TxnType.Payment,
        Gtxn[9].amount() == Int(int(price * 62500)),
        Gtxn[9].receiver() == Addr(COLLAB_5_ADDRESS),
        Gtxn[9].close_remainder_to() == Global.zero_address(),
        # pay collaborator 6 6.25% of the sale
        Gtxn[10].type_enum() == TxnType.Payment,
        Gtxn[10].amount() == Int(int(price * 62500)),
        Gtxn[10].receiver() == Addr(COLLAB_6_ADDRESS),
        Gtxn[10].close_remainder_to() == Global.zero_address(),
        # pay collaborator 7 6.25% of the sale
        Gtxn[11].type_enum() == TxnType.Payment,
        Gtxn[11].amount() == Int(int(price * 62500)),
        Gtxn[11].receiver() == Addr(COLLAB_7_ADDRESS),
        Gtxn[11].close_remainder_to() == Global.zero_address(),
        # pay collaborator 8 6.25% of the sale
        Gtxn[12].type_enum() == TxnType.Payment,
        Gtxn[12].amount() == Int(int(price * 62500)),
        Gtxn[12].receiver() == Addr(COLLAB_8_ADDRESS),
        Gtxn[12].close_remainder_to() == Global.zero_address(),
    )

    cancel = And(
        # opt in seller
        Gtxn[0].type_enum() == TxnType.AssetTransfer,
        Gtxn[0].asset_amount() == Int(0),
        Gtxn[0].sender() == Gtxn[0].asset_receiver(),
        Gtxn[0].asset_close_to() == Global.zero_address(),
        Gtxn[0].xfer_asset() == Int(asset_index),
        Gtxn[0].asset_receiver() == Addr(seller),
        # close asset to seller
        Gtxn[1].type_enum() == TxnType.AssetTransfer,
        Gtxn[1].asset_amount() == Int(1),
        Gtxn[1].xfer_asset() == Int(asset_index),
        Gtxn[1].asset_receiver() == Addr(seller),
        Gtxn[1].asset_close_to() == Addr(seller),
        # close escrow remainder to seller
        Gtxn[2].type_enum() == TxnType.Payment,
        Gtxn[2].amount() == Int(0),
        Gtxn[2].sender() == Gtxn[1].sender(),
        Gtxn[2].receiver() == Addr(seller),
        Gtxn[2].close_remainder_to() == Addr(seller),
    )

    security = And(
        Txn.fee() <= Global.min_txn_fee(),
        Txn.lease() == Global.zero_address(),
        Txn.rekey_to() == Global.zero_address(),
    )

    contract_py = And(
        security,
        Cond(
            [Global.group_size() == Int(3), Or(put_on_sale, cancel)],
            [Global.group_size() == Int(13), buy_asset],
        ),
    )

    return compileTeal(contract_py, Mode.Signature, version=6)
