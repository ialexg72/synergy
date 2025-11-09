#pragma once

template <typename T>
class BinaryTree {
public:
    virtual ~BinaryTree() = default;
    virtual void push(const T& value) = 0;
    virtual T pop(const T& value) = 0;   // удаляет и возвращает значение, если найдено
    virtual bool search(const T& value) const = 0;
    virtual bool empty() const = 0;
};