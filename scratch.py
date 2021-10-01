A = [0,0,0,0,0]
B = [1,2,3]
A.append(B)
print(A)


# import torch 
# from torch.utils.data import TensorDataset, DataLoader

# class SimpleCustomBatch:
#     def __init__(self, data):
#         transposed_data = list(zip(*data))
#         self.inp = torch.stack(transposed_data[0], 0)
#         self.tgt = torch.stack(transposed_data[1], 0)

#     # custom memory pinning method on custom type
#     def pin_memory(self):
#         self.inp = self.inp.pin_memory()
#         self.tgt = self.tgt.pin_memory()
#         return self

# def collate_wrapper(batch):
#     return SimpleCustomBatch(batch)

# inps = torch.arange(10 * 5, dtype=torch.float32).view(10, 5)
# tgts = torch.arange(10 * 5, dtype=torch.float32).view(50, 1)
# print('inps',inps)
# print('tgts',tgts)
# dataset = TensorDataset(inps, tgts)

# loader = DataLoader(dataset, batch_size=2, collate_fn=collate_wrapper,
#                     pin_memory=True)

# for batch_ndx, sample in enumerate(loader):
#     print(sample.inp.is_pinned())
#     print(sample.tgt.is_pinned())


# import torch 

# z = torch.IntTensor([0,1,2,3,4,5,6,7,8,9,10])

# z1 = torch.split(z, 5, dim=0)
# print(*z1,sep='\n')

# A = [0,0,0,0,0]
# B = [1,2,3]

# print(A+B)