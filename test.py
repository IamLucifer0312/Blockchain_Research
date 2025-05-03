from block import Block
import time

if __name__ == "__main__":
    # Create a new block
    block = Block(0, "0", time.time(), "Block data")
    
    # Mine the block with a difficulty of 4
    block.mine_block(4)
    
    # Print the block's hash
    print(f"Block hash: {block.hash}")