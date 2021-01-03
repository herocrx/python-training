import torch, torchvision

# Let’s take a look at a single training step. 
# For this example, we load a pretrained resnet18 model from torchvision. 
# We create a random data tensor to represent a single image with 3 channels, and height & width of 64, and its corresponding label initialized to some random values.

model = torchvision.models.resnet18(pretrained=True)
data = torch.rand(1, 3, 64, 64)
labels = torch.rand(1, 1000)


# Next, we run the input data through the model through each of its layers to make a prediction. This is the forward pass.
prediction = model(data) # forward pass -> point 6 in the book

# We use the model’s prediction and the corresponding label to calculate the error (loss). 
# The next step is to backpropagate this error through the network. 
# Backward propagation is kicked off when we call .backward() on the error tensor. 
# Autograd then calculates and stores the gradients for each model parameter in the parameter’s .grad attribute.

loss = (prediction - labels).sum()
print(f"Your loss equals: {loss}")
loss.backward() # backward pass

# Next, we load an optimizer, in this case SGD with a learning rate of 0.01 and momentum of 0.9. We register all the parameters of the model in the optimizer.
optim = torch.optim.SGD(model.parameters(), lr=1e-2, momentum=0.9)

# Finally, we call .step() to initiate gradient descent. The optimizer adjusts each parameter by its gradient stored in .grad.
optim.step() #gradient descent
prediction = model(data) # forward pass -> point 6 in the book
loss = (prediction - labels).sum()
print(f"Your loss after gradient descen iteration equals: {loss}")
