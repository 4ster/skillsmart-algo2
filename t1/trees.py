class SimpleTreeNode:

    def __init__(self, val, parent):
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.Children = []  # список дочерних узлов


class SimpleTree:

    def __init__(self, root):
        self.Root = root  # корень, может быть None

    # добавляет в узел ParentNode дочерним узел NewChild
    def AddChild(self, ParentNode, NewChild):
        if ParentNode is not None:
            NewChild.Parent = ParentNode
            ParentNode.Children.append(NewChild)
            return True # ваш код добавления нового дочернего узла существующему ParentNode

    # удаляет узел
    def DeleteNode(self, NodeToDelete):
        # не удаляем корень
        if NodeToDelete.Parent is not None:
            NodeToDelete.Parent.Children.remove(NodeToDelete)
            NodeToDelete.Parent = None
            return True  # ваш код удаления существующего узла NodeToDelete

    # возвращает список всех узлов
    def GetAllNodes(self):
        # в случае пустого дерева возвращаем пустой список
        if self.Root is None:
            return []

        # ваш код выдачи всех узлов дерева в определённом
        # добавляем в список всех узлов корень
        all_nodes = [self.Root]

        # заводим список для хранения узлов, у которых будем проверять дочерние
        queue = [self.Root, ]

        # проходим по всем узлам в этом списке
        while len(queue) > 0:
            # забираем один узел
            q = queue.pop()
            # если у него есть дочерние узлы, добавляем их в список всех узлов и всписок для проверки дочерних
            if len(q.Children) > 0:
                queue.extend(q.Children)
                all_nodes.extend(q.Children)

        return all_nodes

    # находит все узлы по заданному значению
    def FindNodesByValue(self, val):
        # ваш код поиска узлов по значению
        if self.Root is None:
            return []
        # список для хранения всех узлов
        all_nodes = []

        # проверяем значение в корне и добавляем, если подходит
        if self.Root.NodeValue == val:
            all_nodes.append(self.Root)

        # в список для поиска дочерних элементов добавляем корень
        queue = [self.Root]

        # пока список не пустой
        while len(queue) > 0:
            # забираем элемент из списка
            q = queue.pop()
            # если у этого элемента есть дочерние
            if len(q.Children) > 0:
                # добавляем их список в список для поиска дочерних
                queue.extend(q.Children)
                # проверяем каждый элемент списка на совпадающие с val значения и добавляем в список всех узлов, если нужно
                for c in q.Children:
                    if c.NodeValue == val:
                        all_nodes.append(c)

        return all_nodes

    # перемещает узел дерева
    def MoveNode(self, OriginalNode, NewParent):
        # ваш код перемещения узла вместе с его поддеревом --
        # в качестве дочернего для узла NewParent
        # удаляем OriginalNode из списка дочерних у его родителя
        OriginalNode.Parent.Children.remove(OriginalNode)

        # задаем новый ролительский узел для OriginalNode
        OriginalNode.Parent = NewParent

        # добавляем OriginalNode в список дочерних узла NewParent
        NewParent.Children.append(OriginalNode)

        return True

    # считает все узлы в дереве
    def Count(self):
        # количество всех узлов в дереве
        cnt = 0
        # если дерево непустое, то считаем корень
        if self.Root is not None:
            cnt += 1
        else:
            return 0
        # добавляем в список для поиска дочерних узлов корень
        queue = [self.Root]

        # пока этот список непустой
        while len(queue) > 0:
            # достаем один элемент
            q = queue.pop()
            # если у него есть дочерние
            if len(q.Children) > 0:
                # добавляем их в список для поиска дочерних элементов
                queue.extend(q.Children)
                # и увеличиваем счетчик на их количество
                cnt += len(q.Children)

        return cnt

    # считает листья в дереве
    def LeafCount(self):
        if self.Root is None:
            return 0

        # количество листьев в дереве
        cnt = 0
        # если в дереве только корень, то это единственный лист - возвращаем 1
        if len(self.Root.Children) == 0:
            return 1
        else:
            # иначе добавляем в список для поиска дочерних элементов корень
            queue = [self.Root]

            # пока этот список непуст
            while len(queue) > 0:
                # достаем из него один элемент
                q = queue.pop()
                # если у этого элемента есть дочерние
                if len(q.Children) > 0:
                    # добавляем их список в список для поиска дочерних
                    queue.extend(q.Children)
                    # проходим по списку дочерних текущего элемента и считаем листья
                    for c in q.Children:
                        if len(c.Children) == 0:
                            cnt += 1

        return cnt

