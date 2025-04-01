### Localisation bluetooth
A simple script using the averaged RSSI of bluetooth beacon to give the position of the receiver. 
The Log-distance path loss model is used ([wiki](https://en.wikipedia.org/wiki/Log-distance_path_loss_model)):

![equation](https://latex.codecogs.com/svg.image?L=L_\text{Tx}-L_\text{Rx}=L_0&plus;10\gamma\log_{10}\frac{d}{d_0}&plus;X_\text{g})  

The RSSI measurement is made with [bluepy](https://pypi.org/project/bluepy/).

Only one RSSI measurement per second is possible (but every beacon at the same time) so the averaging require a bit of time.

![](https://github.com/sreeesjlqkjfkqjsdflkqjsflqjsdflqjf/blueloc/blob/master/image/illustration.png)
