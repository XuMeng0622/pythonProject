SELECT
    goods_inventory_in.goods_id,
    goods_inventory_in.quantity AS total_in_quantity,
    SUM(IFNULL(goods_inventory_out.quantity, 0)) AS total_out_quantity,
    goods_inventory_in.quantity - SUM(IFNULL(goods_inventory_out.quantity, 0)) AS remaining_quantity
FROM
    goods_inventory_in
    LEFT JOIN goods_inventory_out ON goods_inventory_in.goods_id = goods_inventory_out.goods_id
GROUP BY
    goods_inventory_in.goods_id
ORDER BY
    remaining_quantity DESC;


SELECT
    goods_id,
    total_in_quantity,
    total_out_quantity,
    remaining_quantity
FROM
    (
        SELECT
            goods_inventory_in.goods_id,
            goods_inventory_in.quantity AS total_in_quantity,
            SUM(IFNULL(goods_inventory_out.quantity, 0)) AS total_out_quantity,
            goods_inventory_in.quantity - SUM(IFNULL(goods_inventory_out.quantity, 0)) AS remaining_quantity
        FROM
            goods_inventory_in
            LEFT JOIN goods_inventory_out ON goods_inventory_in.goods_id = goods_inventory_out.goods_id
        GROUP BY
            goods_inventory_in.goods_id
    ) AS temp_table
ORDER BY
    remaining_quantity DESC
LIMIT 1;