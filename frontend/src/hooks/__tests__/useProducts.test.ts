import { renderHook } from '@testing-library/react';
import { useProducts } from '../useProducts';
import { Product } from '../../types';

const expectedProducts: Product[] = [
    {
        id: 1,
        name: 'IPhone 14 Pro',
        description: 'Latest iphone, buy it now',
        price: 999,
        priceSymbol: '$',
        category: 'Электроника',
        imgUrl: '/iphone.png',
    },
    {
        id: 2,
        name: 'Костюм гуся',
        description: 'Запускаем гуся, работяги',
        price: 1000,
        priceSymbol: '₽',
        category: 'Одежда',
    },
    {
        id: 3,
        name: 'Настольная лампа',
        description: 'Говорят, что ее использовали в pixar',
        price: 699,
        category: 'Для дома',
        imgUrl: '/lamp.png',
    },
    {
        id: 4,
        name: 'Принтер',
        description: 'Незаменимая вещь для студента',
        price: 7000,
        category: 'Электроника',
    },
];

describe('test useProducts hook', () => {
    it('should return products', () => {
        const { result } = renderHook(() => useProducts());
        expect(result.current).toStrictEqual(expectedProducts);
    });
});
