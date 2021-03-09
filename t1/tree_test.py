import unittest

from trees import SimpleTreeNode, SimpleTree


class SimpleTreeNodeTestCase(unittest.TestCase):
    def test_add_child_for_existing_parent(self):
        # создаем дерево
        parent_node = SimpleTreeNode(0, None)
        tree = SimpleTree(parent_node)

        # создаем и добавляем дочерний узел
        child_node = SimpleTreeNode(1, None)
        tree.AddChild(parent_node, child_node)

        # получаем список значений узлов
        nodes = [x.NodeValue for x in tree.GetAllNodes()]
        nodes = tuple(sorted(nodes))

        # проверяем, что список узлов равен (0, 1)
        self.assertTupleEqual(
            nodes,
            (0, 1)
        )

    def test_add_child_to_empty_tree(self):
        # создаем дерево
        parent_node = None
        tree = SimpleTree(parent_node)

        # создаем и добавляем дочерний узел
        child_node = SimpleTreeNode(1, None)
        tree.AddChild(parent_node, child_node)

        # получаем список узлов
        nodes = [x.NodeValue for x in tree.GetAllNodes()]

        # проверяем, что список пуст
        self.assertEqual(
            len(nodes),
            0
        )

    def test_add_child_existing(self):
        # создаем дерево
        parent_node = SimpleTreeNode(0, None)
        tree = SimpleTree(parent_node)

        # создаем и добавляем дочерний узел
        child_node = SimpleTreeNode(1, None)
        tree.AddChild(parent_node, child_node)

        # снова добавляем его же
        tree.AddChild(parent_node, child_node)

        # получаем список значений узлов
        nodes = [x.NodeValue for x in tree.GetAllNodes()]
        nodes = tuple(sorted(nodes))

        # проверяем, что список значений узлов равен (0, 1, 1)
        self.assertTupleEqual(
            nodes,
            (0, 1, 1)
        )

    def test_remove_child(self):
        # создаем дерево
        parent_node = SimpleTreeNode(0, None)
        tree = SimpleTree(parent_node)

        # создаем и добавляем дочерний узел
        child_node = SimpleTreeNode(1, None)
        tree.AddChild(parent_node, child_node)

        # удаляем дочерний узел
        tree.DeleteNode(child_node)

        # получаем список значений узлов
        nodes = [x.NodeValue for x in tree.GetAllNodes()]
        nodes = tuple(sorted(nodes))

        # проверяем, что список узлов равен (0, )
        self.assertTupleEqual(
            nodes,
            (0,)
        )


    def test_remove_child_non_existing(self):
        # создаем дерево
        parent_node = SimpleTreeNode(0, None)
        tree = SimpleTree(parent_node)

        # создаем узел, но не добавляем
        child_node = SimpleTreeNode(1, None)

        # удаляем не принадлежащий к дереву узел
        tree.DeleteNode(child_node)

        # получаем список значений узлов
        nodes = [x.NodeValue for x in tree.GetAllNodes()]
        nodes = tuple(sorted(nodes))

        # проверяем, что список узлов равен (0,)
        self.assertTupleEqual(
            nodes,
            (0,)
        )

    def test_get_all(self):
        # создаем дерево
        parent_node = SimpleTreeNode(0, None)
        tree = SimpleTree(parent_node)

        # создаем и добавляем дочерние узлы в цикле
        for i in range(1, 5):
            child_node = SimpleTreeNode(i, None)
            tree.AddChild(parent_node, child_node)

        # получаем список значений узлов
        nodes = [x.NodeValue for x in tree.GetAllNodes()]
        nodes = tuple(sorted(nodes))

        # проверяем, что список узлов равен (0,1,2,3,4,)
        self.assertTupleEqual(
            nodes,
            (0, 1, 2, 3, 4,)
        )

    def test_get_all_from_empty(self):
        # создаем дерево
        parent_node = None
        tree = SimpleTree(parent_node)

        # получаем список значений узлов
        nodes = tree.GetAllNodes()

        # проверяем, что список пуст
        self.assertEqual(
            len(nodes),
            0
        )


    def test_find_existing_node_by_val(self):
        # создаем дерево
        parent_node = SimpleTreeNode(0, None)
        tree = SimpleTree(parent_node)

        # создаем и добавляем дочерние узлы
        child_node = SimpleTreeNode(1, None)
        tree.AddChild(parent_node, child_node)

        child_node1 = SimpleTreeNode(2, None)
        tree.AddChild(child_node, child_node1)

        child_node2 = SimpleTreeNode(2, None)
        tree.AddChild(parent_node, child_node2)

        # получаем список узлов
        nodes = tuple(tree.FindNodesByValue(2))

        # проверяем, что длина списка равна 2
        self.assertEqual(
            len(nodes),
            2
        )

    def test_find_in_empty_tree(self):
        # создаем дерево
        parent_node = None
        tree = SimpleTree(parent_node)

        # получаем список значений узлов
        nodes = tree.FindNodesByValue(2)

        # проверяем, что список пуст
        self.assertEqual(
            len(nodes),
            0
        )


    def test_find_non_existing_node_by_val(self):
        # создаем дерево
        parent_node = SimpleTreeNode(0, None)
        tree = SimpleTree(parent_node)

        # создаем и добавляем дочерние узлы
        child_node = SimpleTreeNode(1, None)
        tree.AddChild(parent_node, child_node)

        child_node1 = SimpleTreeNode(2, None)

        # получаем список узлов
        nodes = tuple(tree.FindNodesByValue(2))

        # проверяем, что длина списка равна 0
        self.assertEqual(
            len(nodes),
            0
        )

    def test_move_node(self):
        # создаем дерево
        parent_node = SimpleTreeNode(0, None)
        tree = SimpleTree(parent_node)

        # создаем и добавляем дочерние узлы
        child_node = SimpleTreeNode(1, None)
        tree.AddChild(parent_node, child_node)

        child_node1 = SimpleTreeNode(2, None)
        tree.AddChild(child_node, child_node1)

        # переносим узел
        tree.MoveNode(child_node1, parent_node)

        # проверяем, что родитель поменялся
        child = tree.FindNodesByValue(2)
        print(child)
        self.assertTupleEqual(
            (len(child), child[0].Parent.NodeValue),
            (1, 0)
        )

    def test_count_existing(self):
        # создаем дерево
        parent_node = SimpleTreeNode(0, None)
        tree = SimpleTree(parent_node)

        # создаем и добавляем дочерние узлы
        child_node = SimpleTreeNode(1, None)
        tree.AddChild(parent_node, child_node)

        child_node1 = SimpleTreeNode(2, None)
        tree.AddChild(child_node, child_node1)

        # считаем количество узлов
        cnt = tree.Count()

        # проверяем, что количество узлов совпадает
        self.assertEqual(
            cnt,
            3
        )

    def test_count_of_empty_tree(self):
        # создаем дерево
        parent_node = None
        tree = SimpleTree(parent_node)

        # считаем количество узлов
        cnt = tree.Count()

        # проверяем, что количество узлов совпадает
        self.assertEqual(
            cnt,
            0
        )

    def test_leaf_count_exist(self):
        # создаем дерево
        parent_node = SimpleTreeNode(0, None)
        tree = SimpleTree(parent_node)

        # создаем и добавляем дочерние узлы
        child_node = SimpleTreeNode(1, None)
        tree.AddChild(parent_node, child_node)

        child_node1 = SimpleTreeNode(2, None)
        tree.AddChild(child_node, child_node1)

        # считаем количество листьев
        cnt = tree.LeafCount()

        # проверяем, что количество листьев совпадает
        self.assertEqual(
            cnt,
            1
        )

    def test_count_leaf_of_empty_tree(self):
        # создаем дерево
        parent_node = None
        tree = SimpleTree(parent_node)

        # считаем количество узлов
        cnt = tree.LeafCount()

        # проверяем, что количество узлов совпадает
        self.assertEqual(
            cnt,
            0
        )

    def test_levels(self):
        # создаем дерево
        parent_node = SimpleTreeNode(0, None)
        tree = SimpleTree(parent_node)

        # создаем и добавляем дочерние узлы
        child_node = SimpleTreeNode(1, None)
        tree.AddChild(parent_node, child_node)

        child_node1 = SimpleTreeNode(2, None)
        tree.AddChild(child_node, child_node1)

        tree.SetLevels()

        self.assertTupleEqual(
            (parent_node.Level, child_node.Level, child_node1.Level),
            (0, 1, 2)
        )


if __name__ == '__main__':
    unittest.main()
