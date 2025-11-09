#pragma once

template <typename T>
class Queue {
public:
    virtual ~Queue() = default;
    virtual void push(const T& value) = 0;
    virtual T pop() = 0;           // предполагается, что очередь не пуста
    virtual bool empty() const = 0;
};