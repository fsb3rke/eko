# eko
Sımple Economy Library

## Usage

### PROFILE

Create Profile
```python
profile("profile_id").create()
```
Get Profile
```python
profile("profile_id").get()
```
### COIN

Add Coin
```python
money = 100
coin("profile_id").add(money)
```
Remove Coin
```python
money = 100
coin("profile_id").remove(money)
```
Transfer Coin
```python
money = 100
coin("profile_id").transfer("target_profile_id", money)
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
