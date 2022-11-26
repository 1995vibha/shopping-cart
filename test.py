class Product(object):
    def __init__(self, product_id, name, price, qty, gst=0):
        self.product_id = product_id
        self.product_name = name
        self.price = price
        self.qty = qty
        self.gst = gst
        self.discount = 0
        self.product_total = self.price * self.qty  #without discount
        if self.price >= 500:
            self.discount = (self.product_total * self.discount) / 100

        self.gst_amount = ((self.product_total - self.discount) * self.gst) * 100
        self.product_final_amount = (self.product_total - self.discount) + self.gst_amount


class Cart(object):
    def __init__(self):
        self.content = dict()

    def update(self, product):
        if product.product_id not in self.content:
            self.content.update({product.product_id: product})
            return
        for k, v in self.content.get(product.product_id).iteritems():
            if k == 'product_id':
                continue
            elif k == 'qty':
                total_qty = v.qty + product.qty
                if total_qty:
                    v.qty = total_qty
                    continue
                self.remove_product(k)
            else:
                v[k] = product[k]

    def get_total(self):
        #return total of cart
        return sum([v.product_final_amount for _, v in self.content.iteritems()])

    def get_num_products(self):
        return sum([v.qty for _, v in self.content.iteritems()])

    def remove_product(self, key):
        self.content.pop(key)

    def max_gst_product(self):
        return max([v.gst_amount for _, v in self.content.iteritems()])