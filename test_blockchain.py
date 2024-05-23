import unittest
from urllib import response

from blockchain import Blockchain

class TestBlockchain(unittest.TestCase):
    def setUp(self):
        self.blockchain = Blockchain()

    def test_genesis_block(self):
        #Testing if the genesis block is created correctly
        genesis_block = self.blockchain.chain[0]
        self.assertEqual(genesis_block['index'],1)
        self.assertEqual(genesis_block['proof'], 100)
        self.assertEqual(genesis_block['previous_hash'],1)
    def test_new_transaction(self):
        #Test if a new Transaction is added correctly
        self.blockchain.new_transaction("Juba", "Ales", 50)
        self.assertEqual(len(self.blockchain.current_transactions), 1)
        self.assertEqual(self.blockchain.current_transactions[0]['sender'], "Juba")
        self.assertEqual(self.blockchain.current_transactions[0]['recipient'], "Ales")
        self.assertEqual(self.blockchain.current_transactions[0]['amount'], 50)

    def test_new_block(self):
        #Test if a new block is properly created
        self.blockchain.new_transaction("Juba", "Ales", 50)
        previous_hash = self.blockchain.hash(self.blockchain.last_block)
        new_block = self.blockchain.new_block(12345, previous_hash)
        self.assertEqual(new_block['index'], 2)
        self.assertEqual(new_block['proof'], 12345)
        self.assertEqual(new_block['previous_hash'], previous_hash)
        self.assertEqual(len(new_block['transactions']), 1)

    def test_new_proof_of_work(self):
        #Testing if the proof of work is appropriate
        last_proof = self.blockchain.last_block['proof']
        proof = self.blockchain.proof_of_work(last_proof)
        self.assertTrue(self.blockchain.valid_proof(last_proof, proof))

    def test_full_chain(self):
        #Testing if the full chain is appropriately returned
        response = {
        'chain': self.blockchain.chain,
        'length': len(self.blockchain.chain),
        }

        self.assertEqual(response['length'], len(self.blockchain.chain))
        self.assertEqual(response['chain'], self.blockchain.chain)

if __name__ == '__main__':
        unittest.main()