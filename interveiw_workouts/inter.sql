select
    c.city_name,
    p.product_name,
    ROUND(sum(it.line_total_price), 2) as price
from
    city c,
    customer cu,
    invoice i,
    invoice_item it,
    product p
where
    c.id = cu.city_id
    and cu.id = i.customer_id
    and i.id = it.invoice_id
    and it.product_id = p.id
group by
    c.city_name,
    p.product_name
order by
    price desc,
    c.city_name,
    p.product_name

    