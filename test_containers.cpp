#include <gtest/gtest.h>
#include "queue_interface.h"
#include "heap_interface.h"
#include "binary_tree_interface.h"

// -----------------------
// Mock-реализации (для тестирования интерфейсов)
// -----------------------

template <typename T>
class MockQueue : public Queue<T> {
    std::vector<T> data;
public:
    void push(const T& value) override { data.push_back(value); }
    T pop() override {
        T val = data.front();
        data.erase(data.begin());
        return val;
    }
    bool empty() const override { return data.empty(); }
};

template <typename T>
class MockHeap : public Heap<T> {
    std::vector<T> data;
public:
    void push(const T& value) override { data.push_back(value); }
    T pop() override {
        auto max_it = std::max_element(data.begin(), data.end());
        T val = *max_it;
        data.erase(max_it);
        return val;
    }
    bool empty() const override { return data.empty(); }
};

template <typename T>
class MockBinaryTree : public BinaryTree<T> {
    std::set<T> data;
public:
    void push(const T& value) override { data.insert(value); }
    T pop(const T& value) override {
        auto it = data.find(value);
        if (it != data.end()) {
            T val = *it;
            data.erase(it);
            return val;
        }
        throw std::runtime_error("Value not found");
    }
    bool search(const T& value) const override { return data.find(value) != data.end(); }
    bool empty() const override { return data.empty(); }
};

// -----------------------
// Тесты
// -----------------------

TEST(QueueTest, PushAndPop) {
    MockQueue<int> q;
    q.push(10);
    q.push(20);
    EXPECT_FALSE(q.empty());
    EXPECT_EQ(q.pop(), 10);
    EXPECT_EQ(q.pop(), 20);
    EXPECT_TRUE(q.empty());
}

TEST(HeapTest, PushAndPopMax) {
    MockHeap<int> h;
    h.push(5);
    h.push(15);
    h.push(10);
    EXPECT_FALSE(h.empty());
    EXPECT_EQ(h.pop(), 15);
    EXPECT_EQ(h.pop(), 10);
    EXPECT_EQ(h.pop(), 5);
    EXPECT_TRUE(h.empty());
}

TEST(BinaryTreeTest, PushSearchPop) {
    MockBinaryTree<int> tree;
    tree.push(10);
    tree.push(5);
    tree.push(15);
    EXPECT_TRUE(tree.search(10));
    EXPECT_TRUE(tree.search(5));
    EXPECT_FALSE(tree.search(20));
    EXPECT_EQ(tree.pop(10), 10);
    EXPECT_FALSE(tree.search(10));
    EXPECT_TRUE(tree.search(5));
    EXPECT_FALSE(tree.empty());
    tree.pop(5);
    tree.pop(15);
    EXPECT_TRUE(tree.empty());
}